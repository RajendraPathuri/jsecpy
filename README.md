# JSecPy: Python-Based Java Security Analyzer for OWASP Top 10 Vulnerabilities

`Jsecpy` is a command-line tool for analyzing Java code for security vulnerabilities based on OWASP Top 10. It uses a combination of code parsing and pattern matching to detect potential vulnerabilities, and provides suggestions for resolving them.

## Requirements

To run the tool, you need to have the following dependencies installed:

- Python 3.x
- `pip` package manager

To install the required dependencies, run:

pip install -r requirements.txt


## Usage

To analyze a Java file, run:

python main.py path/to/java/file.java

The tool will analyze the file and output any detected vulnerabilities along with suggestions for resolving them.

## File structure

The file structure of the tool is as follows:

- `main.py`: Entry point of the command-line tool
- `README.md`: Documentation
- `requirements.txt`: List of dependencies
- `javalyzer/`: Package containing the main logic of the tool
    - `__init__.py`
    - `analyzer.py`: Main logic for analyzing Java files
    - `vulnerability_detector.py`: Logic for detecting vulnerabilities based on OWASP Top 10
    - `parser.py`: Java code parser
    - `suggestions.py`: Generates suggestions for resolving vulnerabilities
    - `utils.py`: Helper functions
    - `data/`: Data directory containing vulnerability data and patterns
        - `owasp_top_10.json`: OWASP Top 10 vulnerability data
        - `vulnerability_patterns.py`: Vulnerability patterns for matching Java code
- `tests/`: Test suite for the tool
    - `__init__.py`
    - `test_analyzer.py`
    - `test_vulnerability_detector.py`
    - `test_parser.py`
    - `test_suggestions.py`
    - `test_utils.py`
