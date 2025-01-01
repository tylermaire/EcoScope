# EcoScope Project

## Overview
The EcoScope project is a specialized initiative aimed at creating an advanced tool for 16S rRNA analysis. The project focuses on smaller-scale research applications, providing scientists with customizable and efficient tools for microbial community analysis. The tool is being developed using Python and R, with a focus on usability, innovation, and scalability.

## Project Directory Structure
The project files are organized systematically for easy navigation and maintainability:

```
C:\EcoScope\16SAnalyzer\
│
├── .venv\                     # Virtual environment for dependency management
├── data\                      # Directory for input data
├── output\                    # Directory for storing output files
├── results\                   # Directory for analysis results
├── src\                       # Source code for the application
├── test_data\                 # Directory for dummy data used for testing
├── test_output\               # Directory for test output files
├── tests\                     # Test scripts for validating functionality
├── tools\                     # Additional tools or utilities for analysis
├── kraken2_batch_processor.py # Script for batch processing with Kraken2
├── visualize_kraken_results.py# Script for visualizing Kraken2 results
├── README.md                   # Project documentation
```

### Key File Paths
- **Input Data Directory**: `C:\EcoScope\16SAnalyzer\data\`
- **Output Data Directory**: `C:\EcoScope\16SAnalyzer\output\`
- **Results Directory**: `C:\EcoScope\16SAnalyzer\results\`
- **Test Data Directory**: `C:\EcoScope\16SAnalyzer\test_data\`
- **Test Scripts Directory**: `C:\EcoScope\16SAnalyzer\tests\`
- **Visualization Script**: `C:\EcoScope\16SAnalyzer\visualize_kraken_results.py`

## Development Environment
- **IDE**: PyCharm Professional for Python development
- **Programming Languages**: Python, R
- **Operating System**: Ubuntu and Windows environments

## Features and Goals
### Current Features
1. **Sequence Quality Report Generation**:
   - Developed a script using Biopython to calculate and report essential sequence metrics:
     - **Sequence Length**: Provides an overview of the distribution of read lengths.
     - **GC Content**: Calculates the percentage of guanine and cytosine nucleotides.
     - **N50**: Computes the N50 statistic for assembly quality assessment.
     - **Duplication Level**: Evaluates the redundancy within the sequence data.
     - **GC Skew**: Analyzes nucleotide bias for biological insights.
     - **Read Length Distribution**: Generates a detailed histogram of read lengths.

2. **Kraken2 Integration**:
   - Batch processing script for taxonomic classification using Kraken2.
   - Visualization script to create insightful visual representations of Kraken2 results.

3. **Test Environment**:
   - Set up a structured testing framework to ensure robust performance of scripts and modules.

### Project Goals
1. **Innovative Features**:
   - Develop advanced visualizations, such as:
     - Heatmaps for microbial abundance.
     - Interactive charts for data exploration.
   - Implement customizable pipelines to allow researchers to:
     - Define trimming parameters.
     - Modify analysis steps as per experimental needs.

2. **Support for Multiple File Formats**:
   - Ensure compatibility with both FASTQ and FASTA file formats for versatility.

3. **Ease of Use**:
   - Create a user-friendly interface and documentation to simplify tool integration into research workflows.
   - Design the tool with scalability in mind, allowing researchers to analyze datasets of varying sizes.

## Key Achievements
- **Script Development**:
  - Successfully developed and validated a Biopython-based quality report generator.
  - Created scripts for Kraken2 batch processing and result visualization.
- **Organized Project Structure**:
  - Established a well-defined directory layout to streamline development and testing workflows.
- **Tool Accessibility**:
  - Prepared a dummy FASTQ file for testing core functionalities.

## Future Work
1. **Core Functionality**:
   - Finalize the main analysis pipeline for 16S rRNA sequence data.
2. **Data Visualization**:
   - Integrate advanced visualization techniques to improve data interpretation.
3. **Pipeline Customization**:
   - Enhance user configurability for analysis parameters and processing steps.
4. **Testing and Validation**:
   - Expand test cases to cover edge scenarios and larger datasets.
5. **Documentation**:
   - Develop comprehensive user manuals and examples for ease of adoption.

## GitHub Repository
All source code, test scripts, and project documentation are hosted on GitHub:
[Tyler's GitHub](https://github.com/tylermaire)

## Contact
**Developer**: Tyler Maire  
**GitHub Profile**: [tylermaire](https://github.com/tylermaire)
