#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
from prettytable import PrettyTable

from analyzer import analyze_java_file
from suggestions import generate_suggestions
from file_io import read_file, write_file

def main():
    parser = argparse.ArgumentParser(description="This is a tool for analyzing Java files for vulnerabilities and suggesting ways to resolve them using the OWASP Top 10 Vulnerabilities.")
    parser.add_argument("java_file", help="The path to the Java file to be analyzed")
    parser.add_argument("-output", help="The path to the output file where the results will be stored. If not provided, results will be printed to the console.")
    args = parser.parse_args()

    java_file = Path(args.java_file)
    
    if not java_file.exists() or java_file.suffix != ".java":
        print("Error: Invalid Java file path. Please provide a valid Java file.")
        sys.exit(1)

    java_code = read_file(java_file)
    vulnerabilities = analyze_java_file(java_code)
    suggestions = generate_suggestions(vulnerabilities)

    if not vulnerabilities:
        output_str = "No vulnerabilities found in the Java file."
    else:
        vuln_table = PrettyTable()
        vuln_table.field_names = ["OWASP Rank", "Vulnerability Detected", "Library", "Risk Level"]
        for vulnerability in vulnerabilities:
            vuln_table.add_row([vulnerability['owasp_rank'], vulnerability['name'], vulnerability['description'], vulnerability['risk_level']])
        
        # Group suggestions based on vulnerability
        sug_dict = {}
        for suggestion in suggestions:
            vulnerability = suggestion['vulnerability']
            if vulnerability in sug_dict:
                sug_dict[vulnerability].append(suggestion['suggestion'])
            else:
                sug_dict[vulnerability] = [suggestion['suggestion']]
        
        sug_table = PrettyTable()
        sug_table.field_names = ["Vulnerability", "Suggestion"]
        sug_table.align["Vulnerability"] = "l"
        sug_table.align["Suggestion"] = "l"
        for vulnerability, suggestions in sug_dict.items():
            sug_table.add_row([vulnerability, "\n".join(suggestions)])

        output_str = f"Vulnerabilities found:\n{vuln_table}\n\nSuggestions for resolving vulnerabilities:\n{sug_table}"


    if args.output:
        output_file = Path(args.output)
        write_file(output_file, output_str)
        print(f"Results have been written to {output_file}")
    else:
        print(output_str)

if __name__ == "__main__":
    print("                                                                            ");
    print("                                                                            ");
    print("     ██  █████  ██    ██  █████  ███████ ██   ██ ██ ███████ ██      ██████  ");
    print("     ██ ██   ██ ██    ██ ██   ██ ██      ██   ██ ██ ██      ██      ██   ██ ");
    print("     ██ ███████ ██    ██ ███████ ███████ ███████ ██ █████   ██      ██   ██ ");
    print("██   ██ ██   ██  ██  ██  ██   ██      ██ ██   ██ ██ ██      ██      ██   ██ ");
    print(" █████  ██   ██   ████   ██   ██ ███████ ██   ██ ██ ███████ ███████ ██████  ");
    print("                                                                            ");
    print("   -h for help          -output to get result in a new file                 ");
    print("                                                                            ");
    print("                                                                            ");
    main()
