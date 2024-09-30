# analyzer.py

#import re
#from typing import List, Dict

#from .vulnerability_detector import detect_vulnerabilities
#from ..data.vulnerability_patterns import vulnerability_patterns

import re
from pathlib import Path
from typing import List, Dict

from file_io import read_file
from vulnerability_detector import detect_vulnerabilities
from vulnerability_patterns import vulnerability_patterns

def analyze_java_file(java_code: str) -> List[Dict]:
    """
    Analyzes the given Java code for vulnerabilities based on OWASP Top 10.
    
    :param java_code: The Java code to analyze
    :return: A list of detected vulnerabilities
    """
    detected_vulnerabilities = []

    for vulnerability, pattern in vulnerability_patterns.items():
        matches = re.finditer(pattern, java_code, re.MULTILINE)
        
        for match in matches:
            detected_vulnerabilities.append({
                "name": vulnerability,
                "description": match.string[match.start():match.end()],
            })

    vulnerabilities = detect_vulnerabilities(detected_vulnerabilities)
    return vulnerabilities
