import sys
import site

# Debugging: Print environment details
print("Python executable being used:", sys.executable)
print("Python version:", sys.version)
print("Python site-packages location:", site.getsitepackages())

import argparse
import os
import matplotlib.pyplot as plt

def main():
    """
    Entry point for the CLI. Parses user arguments and directs to the appropriate pipeline or function.
    """
    parser = argparse.ArgumentParser(
        description="EcoScope 16S Analyzer: Process and analyze 16S rRNA data."
    )

    parser.add_argument("-i", "--input", required=True, help="Path to the input file (FASTA or FASTQ).")
    parser.add_argument("-o", "--output", required=True, help="Path to the output directory where results will be saved.")
    parser.add_argument("-p", "--pipeline", choices=["default", "custom"], default="default", help="Choose between the default or a custom analysis pipeline.")
    parser.add_argument("--trim-length", type=int, help="Set the trimming length for sequencing reads (optional).")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output for debugging or detailed processing steps.")

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
        stats, lengths = trim_and_analyze_fastq(args.input, args.output, args.trim_length, args.verbose)
        print("Sequence Statistics:")
        print(f"Total reads: {stats['total_reads']}")
        print(f"Average read length: {stats['average_length']:.2f}")
        print(f"GC content: {stats['gc_content']:.2f}%")
        generate_length_histogram(lengths, args.output)
    else:
        print("Unsupported input format. Only FASTQ files are currently supported.")
        return

    print("Processing complete.")

def trim_and_analyze_fastq(input_path, output_dir, trim_length, verbose=False):
    """
    Trim sequences in a FASTQ file to the specified length and compute sequence statistics.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "trimmed.fastq")
    total_reads = 0
    total_bases = 0
    gc_count = 0
    lengths = []

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

            # Update statistics
            total_reads += 1
            total_bases += len(trimmed_sequence)
            gc_count += sum(1 for base in trimmed_sequence if base in "GCgc")
            lengths.append(len(trimmed_sequence))

            # Write trimmed entry to output
            outfile.write(f"{header}\n{trimmed_sequence}\n{plus}\n{trimmed_quality}\n")

            if verbose and total_reads % 1000 == 0:
                print(f"Processed {total_reads} reads...")

    # Calculate statistics
    average_length = total_bases / total_reads if total_reads > 0 else 0
    gc_content = (gc_count / total_bases * 100) if total_bases > 0 else 0

    if verbose:
        print(f"Total reads processed: {total_reads}")
        print(f"Trimmed FASTQ file saved to: {output_file}")

    return {
        "total_reads": total_reads,
        "average_length": average_length,
        "gc_content": gc_content,
    }, lengths

def generate_length_histogram(lengths, output_dir):
    """
    Generate a histogram of sequence lengths.
    """
    plt.hist(lengths, bins=30, color='blue', alpha=0.7)
    plt.title("Sequence Length Distribution")
    plt.xlabel("Length (bases)")
    plt.ylabel("Frequency")
    plt.grid(True)
    output_path = os.path.join(output_dir, "sequence_length_histogram.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Histogram saved to: {output_path}")

if __name__ == "__main__":
    main()
