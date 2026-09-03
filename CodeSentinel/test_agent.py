from agent import run_agent


code = """
import subprocess

API_KEY = "secret-123"
PASSWORD = "admin123"

subprocess.call(user_input, shell=True)
"""


result = run_agent(code)

print("\n=== STATUS ===")
print(result["status"])

print("\n=== FIXED CODE ===")
print(result["fixed_code"])

print("\n=== CHANGES ===")

for change in result["changes"]:
    print("-", change["fix"])

print("\n=== VERIFICATION ===")
print(result["verification"])