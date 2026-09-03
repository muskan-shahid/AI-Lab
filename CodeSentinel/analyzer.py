
import ast
import subprocess
import json
import tempfile
import os
import re


def analyze_code(code):
    """
    CodeSentinel AI Security Analyzer

    Checks Python code for:
    1. Syntax errors
    2. Bandit security vulnerabilities
    3. Hardcoded secrets
    """

    results = {
        "syntax_error": None,
        "security_issues": [],
        "status": "SAFE"
    }

    # --------------------------------
    # 1. Check Python syntax
    # --------------------------------
    try:
        ast.parse(code)

    except SyntaxError as e:
        results["syntax_error"] = {
            "line": e.lineno,
            "message": e.msg
        }

        results["status"] = "ERROR"

        return results

    # --------------------------------
    # 2. Detect hardcoded secrets
    # --------------------------------
    secret_patterns = [
        r'(?i)(api[_-]?key)\s*=\s*["\'][^"\']+["\']',
        r'(?i)(password)\s*=\s*["\'][^"\']+["\']',
        r'(?i)(secret[_-]?key)\s*=\s*["\'][^"\']+["\']',
        r'(?i)(token)\s*=\s*["\'][^"\']+["\']'
    ]

    for pattern in secret_patterns:

        matches = re.finditer(pattern, code)

        for match in matches:

            line_number = code[:match.start()].count("\n") + 1

            results["security_issues"].append({
                "test_id": "CUSTOM_SECRET",
                "issue": "Possible hardcoded secret detected.",
                "severity": "HIGH",
                "confidence": "MEDIUM",
                "line": line_number
            })

    # --------------------------------
    # 3. Save code temporarily
    # --------------------------------
    temp_file = None

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as file:

            file.write(code)
            temp_file = file.name

        # --------------------------------
        # 4. Run Bandit
        # --------------------------------
        process = subprocess.run(
            ["bandit", temp_file, "-f", "json"],
            text=True,
            capture_output=True
        )

        if process.stdout:

            try:

                bandit_result = json.loads(
                    process.stdout
                )

                for issue in bandit_result.get(
                    "results",
                    []
                ):

                    results["security_issues"].append({
                        "test_id": issue.get("test_id"),
                        "issue": issue.get("issue_text"),
                        "severity": issue.get("issue_severity"),
                        "confidence": issue.get(
                            "issue_confidence"
                        ),
                        "line": issue.get(
                            "line_number"
                        )
                    })

            except json.JSONDecodeError:
                pass

        # --------------------------------
        # 5. Update status
        # --------------------------------
        if results["security_issues"]:
            results["status"] = "VULNERABLE"

    except Exception as e:

        results["security_issues"].append({
            "test_id": "ANALYZER_ERROR",
            "issue": f"Analyzer error: {str(e)}",
            "severity": "UNKNOWN",
            "confidence": "LOW"
        })

        results["status"] = "ERROR"

    finally:

        # --------------------------------
        # 6. Delete temporary file
        # --------------------------------
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)

    return results

