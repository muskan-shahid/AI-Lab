from analyzer import analyze_code

code = """
import os
import subprocess

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")

subprocess.call(user_input, shell=False)
"""

result = analyze_code(code)

print(result)