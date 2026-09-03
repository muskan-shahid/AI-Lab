import streamlit as st
from agent import run_agent

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CodeSentinel AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS (High-Contrast Dark Theme & Component Fixes)
# ============================================================

st.markdown(
    """
    <style>

    /* Main App Background & Text */
    .stApp {
        background-color: #0d1117 !important;
        color: #f0f6fc !important;
    }

    /* Force global high-contrast text rendering */
    .stApp p, .stApp span, .stApp label, .stApp div {
        color: #e6edf3;
    }

    /* Sidebar Background & High-Contrast Text */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    }

    section[data-testid="stSidebar"] * {
        color: #f0f6fc !important;
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
        color: #8b949e !important;
    }

    /* Hero Banner */
    .hero {
        padding: 35px 40px;
        border-radius: 18px;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        background: linear-gradient(
            135deg,
            rgba(22, 27, 34, 0.95),
            rgba(13, 17, 23, 0.95)
        );
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        color: #ffffff !important;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 21px;
        color: #aeb6c3 !important;
        font-weight: 500;
    }

    .small-text {
        font-size: 16px;
        color: #8b949e !important;
        line-height: 1.6;
    }

    /* Section Headers */
    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #ffffff !important;
        margin-top: 24px;
        margin-bottom: 14px;
    }

    /* Textarea Background & High-Contrast Code Text */
    .stTextArea,
    div[data-baseweb="textarea"],
    div[data-baseweb="base-input"],
    div[data-testid="stTextArea"] > div {
        background-color: #161b22 !important;
        border-radius: 10px !important;
    }

    .stTextArea textarea {
        background-color: #161b22 !important;
        color: #00ffcc !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        caret-color: #ffffff !important;
    }

    .stTextArea textarea:focus {
        border-color: #00e676 !important;
        box-shadow: 0 0 8px rgba(0, 230, 118, 0.3) !important;
    }

    /* Code Block Contrast & Dark Container (st.code) */
    div[data-testid="stCode"] {
        background-color: #161b22 !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }

    div[data-testid="stCode"] pre,
    div[data-testid="stCode"] pre *,
    div[data-testid="stCode"] code,
    div[data-testid="stCode"] code * {
        background-color: #161b22 !important;
        color: #e6edf3 !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
    }

    /* Custom Syntax Highlighting Overrides */
    div[data-testid="stCode"] .token.keyword,
    div[data-testid="stCode"] span[style*="color: rgb(255, 121, 198)"],
    div[data-testid="stCode"] span[style*="color: rgb(0, 0, 255)"] {
        color: #ff79c6 !important;
        font-weight: 600 !important;
    }

    div[data-testid="stCode"] .token.string,
    div[data-testid="stCode"] span[style*="color: rgb(80, 250, 123)"],
    div[data-testid="stCode"] span[style*="color: rgb(0, 128, 0)"] {
        color: #50fa7b !important;
    }

    div[data-testid="stCode"] .token.function,
    div[data-testid="stCode"] span[style*="color: rgb(139, 233, 253)"] {
        color: #8be9fd !important;
    }

    div[data-testid="stCode"] .token.comment {
        color: #6272a4 !important;
        font-style: italic !important;
    }

    /* Metric Cards */
    .metric-card {
        padding: 20px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        background-color: #161b22;
        text-align: center;
    }

    .metric-number {
        font-size: 32px;
        font-weight: 800;
        color: #ffffff !important;
    }

    .metric-label {
        color: #8b949e !important;
        font-size: 14px;
        font-weight: 600;
    }

    /* Primary Action Button (Analyze & Fix Code) */
    .stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 10px;
        font-size: 17px;
        font-weight: 700;
        background-color: #00e676 !important;
        color: #000000 !important;
        border: none !important;
    }

    .stButton > button:hover {
        background-color: #00c853 !important;
        color: #000000 !important;
    }

    /* Download Button High-Contrast Color Combo */
    div[data-testid="stDownloadButton"] > button {
        background-color: #1f6feb !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        transition: all 0.2s ease-in-out !important;
    }

    div[data-testid="stDownloadButton"] > button:hover {
        background-color: #388bfd !important;
        color: #ffffff !important;
        box-shadow: 0 0 10px rgba(56, 139, 253, 0.4) !important;
    }

    div[data-testid="stDownloadButton"] > button p,
    div[data-testid="stDownloadButton"] > button span {
        color: #ffffff !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO BANNER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            🛡️ CodeSentinel AI
        </div>
        <div class="hero-subtitle">
            Autonomous Code Security & Refactoring Agent
        </div>
        <br>
        <div class="small-text">
            Analyze Python code, detect vulnerabilities,
            automatically generate safer code, and verify the fixes.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## 🛡️ CodeSentinel")
    st.caption("AI-powered Python security analysis")

    st.divider()

    st.markdown("### 🔍 What it does")
    st.write("• Detects security vulnerabilities")
    st.write("• Identifies hardcoded secrets")
    st.write("• Detects dangerous functions")
    st.write("• Generates safer code")
    st.write("• Verifies automatic fixes")
    st.write("• Explains vulnerabilities using AI")

    st.divider()

    st.markdown("### 🤖 AI Engine")
    st.success("Gemini connected")
    st.caption("Powered by Gemini API")

# ============================================================
# CODE INPUT AREA
# ============================================================

st.markdown(
    '<div class="section-title">💻 Python Security Scanner</div>',
    unsafe_allow_html=True
)

default_code = """import subprocess

SECRET_KEY = "sk_test_123456789EXAMPLE"

user_input = input("Enter command: ")

result = eval(user_input)

subprocess.run(user_input, shell=True)

print("Using secret:", SECRET_KEY)
"""

code = st.text_area(
    "Paste your Python code below:",
    value=default_code,
    height=320,
    label_visibility="collapsed"
)

# ============================================================
# ANALYZE BUTTON & RESULTS PIPELINE
# ============================================================

if st.button("🔍 Analyze & Fix Code", type="primary"):

    if not code.strip():
        st.warning("Please enter some Python code.")
    else:
        with st.spinner("CodeSentinel AI is analyzing your code..."):
            try:
                result = run_agent(code)
            except Exception as e:
                st.error(f"❌ Analysis failed: {str(e)}")
                st.stop()

        st.divider()

        # ====================================================
        # SUMMARY METRICS
        # ====================================================

        issues = result.get("security_issues", [])

        high_count = sum(1 for issue in issues if issue.get("severity") == "HIGH")
        medium_count = sum(1 for issue in issues if issue.get("severity") == "MEDIUM")
        low_count = sum(1 for issue in issues if issue.get("severity") == "LOW")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">{len(issues)}</div>
                    <div class="metric-label">Security Issues</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">{high_count}</div>
                    <div class="metric-label">High Risk</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">{medium_count}</div>
                    <div class="metric-label">Medium Risk</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">{low_count}</div>
                    <div class="metric-label">Low Risk</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        # ====================================================
        # SECURITY STATUS
        # ====================================================

        st.markdown(
            '<div class="section-title">🛡️ Security Status</div>',
            unsafe_allow_html=True
        )

        status = result.get("status", "UNKNOWN")

        if status == "SAFE":
            st.success("✅ SAFE — No security vulnerabilities detected.")
        elif status == "VULNERABLE":
            st.error("⚠️ VULNERABLE — Security issues detected.")
        else:
            st.warning("⚠️ Code analysis could not be completed.")

        # ====================================================
        # SECURITY ISSUES
        # ====================================================

        st.markdown(
            '<div class="section-title">🚨 Security Issues</div>',
            unsafe_allow_html=True
        )

        if issues:
            selected_severity = st.multiselect(
                "Filter severity:",
                options=["HIGH", "MEDIUM", "LOW"],
                default=["HIGH", "MEDIUM", "LOW"],
                label_visibility="collapsed"
            )

            filtered_issues = [i for i in issues if i.get("severity", "LOW") in selected_severity]

            for issue in filtered_issues:
                severity = issue.get("severity", "UNKNOWN")
                message = issue.get("issue", "Unknown security issue")

                if severity == "HIGH":
                    st.error(f"🔴 HIGH — {message}")
                elif severity == "MEDIUM":
                    st.warning(f"🟠 MEDIUM — {message}")
                elif severity == "LOW":
                    st.info(f"🔵 LOW — {message}")
                else:
                    st.write(f"⚪ {severity} — {message}")
        else:
            st.success("✅ No security issues found.")

        # ====================================================
        # CODE COMPARISON
        # ====================================================

        st.markdown(
            '<div class="section-title">📊 Code Comparison</div>',
            unsafe_allow_html=True
        )

        original_col, fixed_col = st.columns(2)

        with original_col:
            st.markdown("### 📄 Original Code")
            st.code(code, language="python")

        with fixed_col:
            st.markdown("### 🔧 Fixed Code")
            fixed_code_text = result.get("fixed_code", "")
            st.code(fixed_code_text, language="python")

            if fixed_code_text:
                st.download_button(
                    label="💾 Download Fixed Script (.py)",
                    data=fixed_code_text,
                    file_name="remediated_script.py",
                    mime="text/x-python",
                    use_container_width=True
                )

        # ====================================================
        # AUTOMATIC CHANGES
        # ====================================================

        st.markdown(
            '<div class="section-title">📝 Automatic Changes</div>',
            unsafe_allow_html=True
        )

        changes = result.get("changes", [])

        if changes:
            for index, change in enumerate(changes, start=1):
                st.markdown(f"### Fix {index}")
                st.write(f"**🔧 Change:** {change.get('fix', 'N/A')}")
                st.write(f"**💡 Reason:** {change.get('reason', 'N/A')}")

                if index < len(changes):
                    st.divider()
        else:
            st.info("No automatic fixes were necessary.")

        # ====================================================
        # FIX VERIFICATION
        # ====================================================

        st.markdown(
            '<div class="section-title">✅ Fix Verification</div>',
            unsafe_allow_html=True
        )

        verification = result.get("verification", "UNKNOWN")

        if verification == "PASSED":
            st.success("✅ PASSED — The fixed code passed security verification.")
        elif verification == "ISSUES REMAIN":
            st.warning("⚠️ ISSUES REMAIN — Some security issues still need attention.")
        elif verification == "NO CHANGES":
            st.info("ℹ️ No automatic changes were made.")
        else:
            st.info("Verification was not completed.")

        # ====================================================
        # AI EXPLANATION
        # ====================================================

        st.markdown(
            '<div class="section-title">🤖 AI Security Explanation</div>',
            unsafe_allow_html=True
        )

        explanation = result.get("llm_explanation", "").strip()

        if explanation:
            st.info(explanation)
        elif issues:
            fallback_msg = "### 🛡️ Automated Security Analysis Summary\n\n"
            for idx, issue in enumerate(issues, 1):
                msg = issue.get("issue", "Unspecified issue")
                sev = issue.get("severity", "MEDIUM")
                fallback_msg += f"**{idx}. [{sev}] {msg}**\n"

                if "eval" in msg.lower():
                    fallback_msg += "  * *Risk:* `eval()` evaluates untrusted user strings directly, enabling Remote Code Execution (RCE).\n  * *Remediation:* Replaced with `ast.literal_eval()` which restricts parsing strictly to basic Python literals.\n\n"
                elif "secret" in msg.lower() or "key" in msg.lower() or "password" in msg.lower():
                    fallback_msg += "  * *Risk:* Storing plain-text API keys/passwords directly in code exposes credentials in source repositories.\n  * *Remediation:* Extracted values into `os.getenv()` environment variable lookups.\n\n"
                elif "subprocess" in msg.lower() or "shell" in msg.lower():
                    fallback_msg += "  * *Risk:* Shell execution with formatted strings allows arbitrary command injection.\n  * *Remediation:* Tokenized commands into explicit execution lists without invoking shell wrappers.\n\n"

            st.info(fallback_msg)
        else:
            st.success("No security risks were detected in the provided source code.")

        # ====================================================
        # FOOTER
        # ====================================================

        st.divider()

        st.caption("🛡️ CodeSentinel AI • Autonomous Code Security & Refactoring")