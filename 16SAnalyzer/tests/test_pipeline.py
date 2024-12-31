import os
from subprocess import run

# Define paths
test_input_path = "test_data/test_sample.fastq"
test_output_dir = "test_output"

# Create test data directory
os.makedirs("test_data", exist_ok=True)
os.makedirs(test_output_dir, exist_ok=True)

# Create a dummy FASTQ file for testing
dummy_fastq = """\
@SEQ_ID_1
GATTTGGGGTTTAAACCCGTTTGGGA
+
!''*((((***+))%%%++)(%%%%).1
@SEQ_ID_2
TAAACCCGGTTTGGGGAATTTCCCGGG
+
!''*((((***+))%%%++)(%%%%).1
@SEQ_ID_3
GGGTTTAAACCCGTTTGGGGAATTTCC
+
!''*((((***+))%%%++)(%%%%).1
"""

with open(test_input_path, "w") as f:
    f.write(dummy_fastq)

# Define the command to run the pipeline
command = [
    "python",
    "C:\\EcoScope\\16SAnalyzer\\src\\cli.py",
    "-i", test_input_path,
    "-o", test_output_dir,
    "--trim-length", "20",
    "-v"
]

# Run the command and capture the output
result = run(command, capture_output=True, text=True)

# Print results for debugging
print("Pipeline Output:")
print(result.stdout)
print("Pipeline Errors:")
print(result.stderr)

# Check if the output files exist
trimmed_output_path = os.path.join(test_output_dir, "trimmed.fastq")
histogram_output_path = os.path.join(test_output_dir, "sequence_length_histogram.png")

print("\nTest Results:")
if os.path.exists(trimmed_output_path):
    print(f"Trimmed FASTQ output file exists: {trimmed_output_path}")
else:
    print("Trimmed FASTQ output file is missing.")

if os.path.exists(histogram_output_path):
    print(f"Histogram file exists: {histogram_output_path}")
else:
    print("Histogram file is missing.")

# Clean up (optional)
cleanup = input("Do you want to delete test files? (y/n): ").strip().lower()
if cleanup == "y":
    import shutil
    shutil.rmtree("test_data")
    shutil.rmtree(test_output_dir)
    print("Test files cleaned up.")
else:
    print("Test files retained.")