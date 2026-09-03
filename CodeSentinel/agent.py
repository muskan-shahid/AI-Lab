import ast
import os
import re
from google import genai

# ============================================================
# STATIC SECURITY SCANNER (AST & REGEX)
# ============================================================

def analyze_security_ast(code_str: str) -> list:
    """Performs static analysis using Python AST and Regex to find security risks."""
    issues = []

    # 1. Detect Hardcoded Secrets / Passwords via Regex (Assignment matching)
    secret_patterns = [
        (r'sk_live_[0-9a-zA-Z]{24,}', "HIGH", "Hardcoded live API secret key detected."),
        (r'sk_test_[0-9a-zA-Z]{24,}', "LOW", "Possible hardcoded test API key detected."),
        (r'(?i)(api_key|secret|password|token)\s*=\s*["\'][^"\']{4,}["\']', "HIGH", "Possible hardcoded secret or password detected.")
    ]
    
    for pattern, severity, msg in secret_patterns:
        if re.search(pattern, code_str):
            issues.append({"severity": severity, "issue": msg})

    # 2. AST Visitor for Insecure Functions & Subprocess Checks
    try:
        tree = ast.parse(code_str)
        
        for node in ast.walk(tree):
            # Check for eval()
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "eval":
                issues.append({
                    "severity": "MEDIUM",
                    "issue": "Use of possibly insecure function 'eval()' — consider using safer ast.literal_eval."
                })
            
            # Check for exec()
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "exec":
                issues.append({
                    "severity": "HIGH",
                    "issue": "Use of dangerous function 'exec()' allowing arbitrary code execution."
                })

            # Check for subprocess imports/calls
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                names = [alias.name for alias in node.names]
                if "subprocess" in names:
                    issues.append({
                        "severity": "LOW",
                        "issue": "Consider possible security implications associated with the subprocess module."
                    })

            # Check for shell=True in subprocess
            if isinstance(node, ast.Call):
                func_name = ""
                if isinstance(node.func, ast.Attribute):
                    func_name = node.func.attr
                elif isinstance(node.func, ast.Name):
                    func_name = node.func.id

                if func_name in ["run", "Popen", "call", "check_output"]:
                    for kw in node.keywords:
                        if kw.arg == "shell" and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                            issues.append({
                                "severity": "HIGH",
                                "issue": "subprocess call with shell=True identified, severe security risk."
                            })
    except SyntaxError:
        issues.append({
            "severity": "HIGH",
            "issue": "Syntax error in provided code; static analysis incomplete."
        })

    return issues


# ============================================================
# CODE REMEDIATION ENGINE
# ============================================================

def generate_remediation(code_str: str) -> tuple[str, list]:
    """Applies AST/Regex transformation rules to automatically refactor vulnerable code."""
    lines = code_str.splitlines()
    fixed_lines = list(lines)
    changes = []
    imports_to_add = set()

    for idx, line in enumerate(fixed_lines):
        # Remediation 1: Replace eval() with ast.literal_eval()
        if "eval(" in line:
            fixed_lines[idx] = re.sub(r'\beval\(', 'ast.literal_eval(', line)
            imports_to_add.add("import ast")
            changes.append({
                "fix": "Replaced eval() with ast.literal_eval()",
                "reason": "ast.literal_eval() only evaluates safe Python literals, eliminating arbitrary code execution."
            })

        # Remediation 2: Hardcoded Secrets -> os.getenv()
        secret_match = re.search(r'([A-Z_]*SECRET[A-Z_]*|[A-Z_]*KEY[A-Z_]*)\s*=\s*["\'][^"\']+["\']', line)
        if secret_match:
            var_name = secret_match.group(1)
            fixed_lines[idx] = f'{var_name} = os.getenv("{var_name}")'
            imports_to_add.add("import os")
            changes.append({
                "fix": f'Replaced secret assignment with os.getenv("{var_name}")',
                "reason": "Secrets should be stored in environment variables rather than source code."
            })

        # Remediation 3 & 4: Subprocess shell=True & shlex.split
        if "shell=True" in fixed_lines[idx]:
            fixed_lines[idx] = fixed_lines[idx].replace("shell=True", "shell=False")
            changes.append({
                "fix": "Changed shell=True to shell=False",
                "reason": "Disabling shell=True stops command injection vectors."
            })
            
            if "subprocess.run(" in fixed_lines[idx] and "shlex.split(" not in fixed_lines[idx]:
                fixed_lines[idx] = re.sub(r'subprocess\.run\(([^,\)]+)', r'subprocess.run(shlex.split(\1)', fixed_lines[idx])
                imports_to_add.add("import shlex")
                changes.append({
                    "fix": "Wrapped command argument in shlex.split()",
                    "reason": "Tokenizing inputs ensures arguments are parsed safely as an array vector."
                })

    # Prepend required imports while preserving line breaks
    for imp in sorted(imports_to_add):
        if not any(imp in line for line in fixed_lines):
            fixed_lines.insert(0, imp)

    fixed_code = "\n".join(fixed_lines)
    return fixed_code.strip(), changes


# ============================================================
# LAZY-LOADED GEMINI AI EXPLANATION
# ============================================================

def get_ai_explanation(original_code: str, fixed_code: str, issues: list) -> str:
    """Queries Gemini API for security explanation using google-genai SDK safely."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return ""

    try:
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
        You are an expert security engineer. Explain the vulnerabilities found in this Python code and why the fixes make it secure.
        
        Original Code:
        {original_code}
        
        Detected Issues:
        {issues}
        
        Remediated Code:
        {fixed_code}
        
        Keep your explanation concise, professional, and directly actionable.
        """
        
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"[CodeSentinel Warning] AI Explanation Skipped: {e}")
        return ""


# ============================================================
# AGENT PIPELINE ORCHESTRATOR
# ============================================================

def run_agent(code_str: str) -> dict:
    """Main Orchestrator Agent Pipeline for CodeSentinel AI."""
    # Step 1: Analyze original code
    issues = analyze_security_ast(code_str)
    
    # Step 2: Determine status
    status = "SAFE" if not issues else "VULNERABLE"

    # Step 3: Generate refactored code & changes
    fixed_code, changes = generate_remediation(code_str)

    # Step 4: Verify fixes on the remediated code
    remaining_issues = analyze_security_ast(fixed_code)
    critical_remaining = [i for i in remaining_issues if i["severity"] in ["HIGH", "MEDIUM"]]
    
    if not changes:
        verification = "NO CHANGES"
    elif not critical_remaining:
        verification = "PASSED"
    else:
        verification = "ISSUES REMAIN"

    # Step 5: Fetch AI Explanation
    llm_explanation = get_ai_explanation(code_str, fixed_code, issues)

    return {
        "status": status,
        "security_issues": issues,
        "fixed_code": fixed_code,
        "changes": changes,
        "verification": verification,
        "llm_explanation": llm_explanation
    }