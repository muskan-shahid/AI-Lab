# 🛡️ CodeSentinel AI

### Autonomous Python Security & Refactoring Agent

*Detect → Explain → Fix → Verify*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://yhxwjrhjy7remgjjhrhgdy.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LLM](https://img.shields.io/badge/LLM-Google%20Gemini%203.0%20Flash-4285F4?logo=google)](https://ai.google.dev/)

---

## 📌 Project Overview

*CodeSentinel AI* is an AI-powered Python security and refactoring agent designed to help developers identify and resolve common security vulnerabilities in source code.

The agent analyzes Python code, detects potential security issues, explains the risks, generates safer code using *Google Gemini AI*, and re-scans the modified code to verify the improvements.

---

## 🎯 Problem Statement

Developers can unintentionally introduce security vulnerabilities into Python applications.

Common examples include:

* Dangerous use of eval() and exec()
* Command injection through subprocess
* Hardcoded passwords, API keys, or secrets
* Unsafe shell command execution
* Other potentially dangerous coding patterns

These vulnerabilities can lead to *arbitrary code execution, command injection, credential exposure, and system compromise*.

CodeSentinel AI helps developers identify these issues early and provides safer alternatives.

---

## ✨ Key Features

### 🔍 Security Detection

Scans Python source code for potentially dangerous patterns using *AST parsing and regex-based detection*.

### 🔐 Secret Detection

Identifies possible hardcoded credentials, API keys, passwords, and other sensitive values.

### ⚠️ Risk Classification

Classifies detected issues according to severity:

* 🔴 *HIGH*
* 🟠 *MEDIUM*
* 🟢 *LOW*

### 🤖 AI-Powered Explanation

Uses *Google Gemini* to explain:

* What the vulnerability is
* Why it is dangerous
* How it can affect the application
* How it can be fixed

### 🔧 Automatic Refactoring

Generates a safer version of vulnerable code.

### 🔄 Security Verification

The generated code is scanned again to determine whether the identified vulnerability has been resolved.

### 🌐 Interactive Interface

Provides a *Streamlit-based web interface* where users can submit Python code and review the security analysis.

---

# 🧠 System Architecture

CodeSentinel AI follows an autonomous security analysis pipeline. The system receives Python source code, scans it for vulnerabilities, uses AI to explain the detected issues, generates safer code, and finally re-scans the fixed code to verify the result.

text
                         🛡️ CodeSentinel AI
                                │
                                ▼
                     ┌─────────────────────┐
                     │  Python Source Code │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   Security Scanner │
                     │      AST + Regex   │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │  Security Findings │
                     │ Vulnerabilities +  │
                     │    Risk Levels     │
                     └──────────┬──────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
             ┌─────────────┐        ┌─────────────┐
             │  Auto Fixer │        │  Gemini AI  │
             │             │        │ Explanation │
             └──────┬──────┘        └──────┬──────┘
                    │                       │
                    └──────────┬────────────┘
                               ▼
                    ┌─────────────────────┐
                    │     Fixed Code      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Security Re-Scan  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Verification Result │
                    └──────────┬──────────┘
                               │
                         ┌─────┴─────┐
                         ▼           ▼
                    ✅ Secure    ⚠️ Issues
                      Fixed       Remain


### Architecture Components

| Component               | Responsibility                                                 |
| ----------------------- | -------------------------------------------------------------- |
| *Python Source Code*  | Input provided by the developer                                |
| *Security Scanner*    | Detects vulnerabilities using AST and regex                    |
| *Security Findings*   | Identifies vulnerabilities and assigns risk levels             |
| *Gemini AI*           | Explains vulnerabilities and assists with secure fixes         |
| *Auto Fixer*          | Generates safer versions of vulnerable code                    |
| *Security Re-Scan*    | Checks the modified code again                                 |
| *Verification Result* | Determines whether security issues were successfully addressed |

---

# 🤖 Agent PEAS Description

PEAS describes the *Performance Measure, Environment, Actuators, and Sensors* of an intelligent agent.

| PEAS Component              | CodeSentinel AI                                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| *P – Performance Measure* | Accurate vulnerability detection, correct risk classification, secure fixes, successful verification, and clear explanations |
| *E – Environment*         | Python source code, developer codebases, security rules, and static software environments                                    |
| *A – Actuators*           | Generate secure code, explain vulnerabilities, provide recommendations, and produce security reports                         |
| *S – Sensors*             | AST parser, regex pattern matching, source-code analysis, and vulnerability detection rules                                  |

---

## 🌍 Environment Type

CodeSentinel AI operates in a *digital/software environment*.

| Property             | Description                                                                       |
| -------------------- | --------------------------------------------------------------------------------- |
| *Fully Observable* | The agent receives the Python source code provided for analysis                   |
| *Deterministic*    | Static scanning rules generally produce the same result for the same input        |
| *Static*           | The environment remains unchanged unless the developer or agent modifies the code |
| *Single-Agent*     | CodeSentinel AI operates as a single security analysis agent                      |
| *Discrete*         | Vulnerabilities, fixes, and verification steps are handled as distinct actions    |

---

# ⚠️ Vulnerabilities Detected

A *security vulnerability* is a weakness in software that can potentially be exploited to cause harm.

CodeSentinel AI currently focuses on vulnerabilities such as:

### 1. Dangerous eval()

python
user_input = input("Enter expression: ")
result = eval(user_input)


*Risk:* An attacker may provide malicious Python code that gets executed by the application.

---

### 2. Unsafe Shell Execution

python
import subprocess

user_input = input("Enter command: ")
subprocess.run(user_input, shell=True)


*Risk:* Untrusted input may allow command injection and unauthorized operating-system commands.

---

### 3. Hardcoded Secrets

python
API_KEY = "secret_key_123"


*Risk:* Credentials stored directly in source code may be exposed through repositories, logs, or shared code.

---

# 🧠 Technologies Used

| Technology           | Purpose                                              |
| -------------------- | ---------------------------------------------------- |
| *Python*           | Core application and security analysis               |
| *Python AST*       | Structural source-code analysis                      |
| *Regex*            | Pattern-based vulnerability and secret detection     |
| *Google Gemini AI* | Vulnerability explanation and secure code generation |
| *Streamlit*        | Interactive web interface                            |
| *Git & GitHub*     | Version control and project management               |

---

# 🧪 Example

### Vulnerable Python Code

python
import subprocess

user_input = input("Enter command: ")

result = eval(user_input)

subprocess.run(user_input, shell=True)


### CodeSentinel AI Detection

text
HIGH — Dangerous use of eval()

HIGH — subprocess used with shell=True


### AI Analysis

The agent explains the security risks and recommends safer alternatives.

### Automatic Fix

The agent generates a safer version of the vulnerable code.

### Verification

text
Original Code
     ↓
Vulnerability Detected
     ↓
Secure Fix Generated
     ↓
Fixed Code Re-Scanned
     ↓
✅ Security Verification Successful


---

# 🖼️ Dashboard Preview

### 1. Security Scanner & Issue Detection

<p align="center">
  <img src="https://github.com/user-attachments/assets/a8933009-ff2b-440f-aae4-020249f9e637" width="30%">
  <img src="https://github.com/user-attachments/assets/72d4cb66-a26a-4657-b04b-3dfb500a15ee" width="30%">
</p>

### 2. Code Refactoring & AI Explanation

<p align="center">
  <img src="https://github.com/user-attachments/assets/625a91a7-2113-42d0-ad1b-cec0171181c5" width="30%">
  <img src="https://github.com/user-attachments/assets/a5fce8ff-d541-47b8-a106-dc139e3b8ce3" width="30%">
</p>


---

# 🚀 Live Application

*Try CodeSentinel AI online:*

[![Open Live Demo](https://img.shields.io/badge/🚀_Open_Live_Demo-Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://yhxwjrhjy7remgjjhrhgdy.streamlit.app/)

---

# 👩‍💻 Author

*Muskan Shahid*

BS Computer Science
Federal Urdu University of Arts, Sciences & Technology

---

## 📄 Project Summary

> *CodeSentinel AI* is an autonomous Python security and refactoring agent that detects vulnerabilities, explains security risks, generates safer code using AI, and verifies the resulting code through automated re-scanning.

*Detect. Explain. Fix. Verify.*
