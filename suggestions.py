# suggestions.py

from typing import List, Dict

suggestion_templates = {
    "Broken Access Control": "Implement proper access controls, role-based access, and authorization checks.",
    "Cryptographic Failures": "Sanitize user input and use secure libraries to prevent XSS attacks.",
    "Injection": "Use prepared statements with parameterized queries to prevent SQL injection.",
    "Insecure Design": "Validate and sanitize serialized data before deserialization.",
    "Security Misconfiguration": "Regularly review configurations, use security-hardened defaults, and follow best practices.",
    "Vulnerable and Outdated Components": "Use encryption and proper access controls to protect sensitive data.",
    "Identification & Authentication Failures": "Use anti-CSRF tokens and validate the origin of requests.",
    "Software and data Integrity Failures": "Keep libraries and components up to date, and remove unused dependencies.",
    "Security Logging and Monitoring Failures": "Implement proper logging and monitoring, and set up alerts for suspicious activities.",
    "Server-Side Request Forgery": "Disable XML external entity processing and use secure parsers to prevent XXE attacks.",
}


def generate_suggestions(vulnerabilities: List[Dict]) -> List[Dict]:
    """
    Generates suggestions for resolving the detected vulnerabilities.

    :param vulnerabilities: The list of detected vulnerabilities
    :return: A list of suggestions for resolving the vulnerabilities
    """
    unique_suggestions = {}

    for vulnerability in vulnerabilities:
        vulnerability_name = vulnerability["name"]
        if vulnerability_name in suggestion_templates:
            unique_suggestions[vulnerability_name] = suggestion_templates[vulnerability_name]

    suggestions = [{"vulnerability": k, "suggestion": v} for k, v in unique_suggestions.items()]

    return suggestions


