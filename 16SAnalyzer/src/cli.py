import argparse
import os

def main():
    """
    Entry point for the CLI. Parses user arguments and directs to the appropriate pipeline or function.
    """
    parser = argparse.ArgumentParser(
        description="EcoScope 16S Analyzer: Process and analyze 16S rRNA data."
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to the input file (FASTA or FASTQ)."
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Path to the output directory where results will be saved."
    )
    parser.add_argument(
        "-p", "--pipeline",
        choices=["default", "custom"],
        default="default",
        help="Choose between the default or a custom analysis pipeline."
    )
    parser.add_argument(
        "--trim-length",
        type=int,
        help="Set the trimming length for sequencing reads (optional)."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output for debugging or detailed processing steps."
    )

    args = parser.parse_args()

    if args.verbose:
        print(f"Input file: {args.input}")
        print(f"Output directory: {args.output}")
        print(f"Pipeline: {args.pipeline}")
        if args.trim_length:
            print(f"Trim length: {args.trim_length}")

    # Process data based on pipeline
    process_data(args)

def process_data(args):
    """
    Process the input data based on the provided arguments.
    """
    if args.input.endswith(".fastq"):
        if args.verbose:
            print("Detected FASTQ input format.")
        trim_fastq(args.input, args.output, args.trim_length, args.verbose)
    else:
        print("Unsupported input format. Only FASTQ files are currently supported.")
        return

    print("Processing complete.")

def trim_fastq(input_path, output_dir, trim_length, verbose=False):
    """
    Trim sequences in a FASTQ file to the specified length and save the output.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "trimmed.fastq")
    trimmed_count = 0

    with open(input_path, "r") as infile, open(output_file, "w") as outfile:
        while True:
            # FASTQ files have 4-line entries
            header = infile.readline().strip()
            if not header:  # EOF
                break
            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            quality = infile.readline().strip()

            # Trim sequence and quality
            trimmed_sequence = sequence[:trim_length] if trim_length else sequence
            trimmed_quality = quality[:trim_length] if trim_length else quality

            # Write trimmed entry to output
            outfile.write(f"{header}\n{trimmed_sequence}\n{plus}\n{trimmed_quality}\n")
            trimmed_count += 1

            if verbose and trimmed_count % 1000 == 0:
                print(f"Trimmed {trimmed_count} reads...")

    if verbose:
        print(f"Total reads trimmed: {trimmed_count}")
    print(f"Trimmed FASTQ file saved to: {output_file}")

if __name__ == "__main__":
    main()
