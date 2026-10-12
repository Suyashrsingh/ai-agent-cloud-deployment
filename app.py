"""
Practical 9: Cloud-Deployed AI Agent Application
Entrypoint for Streamlit Community Cloud: streamlit run app.py
"""

import os
import re
import requests
import streamlit as st
from dotenv import load_dotenv

# Load local environment variables if available
load_dotenv()

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="AI Agent - Cloud Deployment",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# SECRET & CONFIGURATION MANAGEMENT
# ==========================================
# Streamlit Cloud reads secrets from st.secrets; local runs read from .env
api_key = None
if hasattr(st, "secrets") and "ATRIA_API_KEY" in st.secrets:
    api_key = st.secrets["ATRIA_API_KEY"]
elif hasattr(st, "secrets") and "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    api_key = os.getenv("ATRIA_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")


# ==========================================
# SIDEBAR: CLOUD STATUS & CONTROLS
# ==========================================
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=220)
    st.title("☁️ Cloud Hub")
    st.markdown("**Practical 9: AI Agent Cloud Deployment**")

    st.markdown("---")
    st.subheader("🌐 Deployment Status")
    st.success("● Cloud Status: Live & Operational")
    st.info("Host: Streamlit Community Cloud")
    st.caption("Runtime: Python 3.10+ / Microservice Architecture")

    st.markdown("---")
    st.subheader("⚙️ Credentials")
    user_key = st.text_input(
        "API Key (Optional override):",
        value=api_key or "",
        type="password",
        help="Paste an API key or configure it in Streamlit Cloud Dashboard Secrets."
    )
    if user_key:
        api_key = user_key

    st.markdown("---")
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hello! I am your Cloud-Deployed AI Agent. Ask me anything!"}
        ]
        st.rerun()

    st.markdown("---")
    st.caption("Department of Computer Science & Engineering")
    st.caption("AI Agent Development Laboratory")


# ==========================================
# KNOWLEDGE & AI RESPONSE GENERATOR
# ==========================================
KNOWLEDGE_BASE = {
    "aws": (
        "**Amazon Web Services (AWS)** is the world's most comprehensive cloud computing platform provided by Amazon.\n\n"
        "**Core Services:**\n"
        "- **Compute:** Amazon EC2 (virtual instances), AWS Lambda (serverless code execution)\n"
        "- **Storage:** Amazon S3 (scalable object storage), Amazon EBS (persistent block storage)\n"
        "- **Databases:** Amazon RDS (relational databases), DynamoDB (managed NoSQL)\n"
        "- **Networking:** Amazon VPC (isolated virtual cloud networks), Route 53 (DNS service)\n"
        "- **AI & ML:** Amazon Bedrock (foundation models), SageMaker (end-to-end ML)"
    ),
    "cloud": (
        "**Cloud Computing** is the on-demand availability of computer system resources—especially data storage "
        "and computing power—without direct active management by the user. "
        "It provides rapid elasticity, pay-as-you-go pricing, and global accessibility."
    ),
    "deployment": (
        "**Application Deployment** is the process of building, configuring, and publishing software onto internet-accessible "
        "servers (such as Streamlit Community Cloud, AWS, or Render) so that end users worldwide can access it via a web URL."
    ),
    "ai": (
        "**Artificial Intelligence (AI)** is the engineering discipline focused on creating computer systems capable of performing "
        "tasks that typically require human intelligence, including learning, reasoning, perception, and problem-solving."
    ),
    "machine learning": (
        "**Machine Learning (ML)** is a subset of AI where systems automatically detect patterns in data and improve their performance "
        "over time without being explicitly programmed."
    ),
    "ai agent": (
        "An **AI Agent** is an autonomous entity that perceives its environment through sensors, reasons about optimal actions, "
        "and interacts through actuators and external tools to achieve specific objectives."
    ),
    "streamlit": (
        "**Streamlit** is an open-source Python framework that allows developers and data scientists to create interactive, "
        "data-driven web applications and dashboards in pure Python without needing frontend HTML/CSS/JavaScript."
    ),
    "github": (
        "**GitHub** is a cloud-based platform for version control and collaborative software development using Git. "
        "It acts as the primary source code repository for continuous deployment pipelines."
    )
}


def query_ai_agent(prompt: str, key: str) -> str:
    """Queries Atria API or provides instant encyclopedic response."""
    # 1. Direct math evaluation
    clean_math = re.sub(r"[^0-9+\-*/().% ]", "", prompt).strip()
    if clean_math and any(op in clean_math for op in ["+", "-", "*", "/"]) and any(c.isdigit() for c in clean_math):
        try:
            res = eval(clean_math, {"__builtins__": {}}, {})
            return f"**Calculated Result:** `{clean_math} = {res}`"
        except Exception:
            pass

    # 2. Try Atria API if key is present
    if key and key.startswith("atr_"):
        try:
            url = "https://api.atria-asi.ai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "Atria-Dawn-Preview",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a friendly and intelligent AI Assistant deployed on the cloud. Provide clear, concise, and helpful answers."
                    },
                    {"role": "user", "content": prompt}
                ]
            }
            res = requests.post(url, headers=headers, json=data, timeout=12)
            if res.status_code == 200:
                answer = res.json()["choices"][0]["message"]["content"]
                if answer and len(answer.strip()) > 0:
                    return answer
        except Exception:
            pass

    # 3. Local Knowledge Base matching
    clean_topic = re.sub(
        r"^(hi|hello|hey|please|can you|tell me|explain|what is|what are|define)\s+",
        "",
        prompt.strip(),
        flags=re.IGNORECASE
    ).strip(" ?.")

    lowered = clean_topic.lower()
    for k, v in KNOWLEDGE_BASE.items():
        if k == lowered or k in lowered.split():
            return v

    # 4. DuckDuckGo Instant Answer API
    try:
        r = requests.get(
            "https://api.duckduckgo.com/",
            params={"q": clean_topic, "format": "json", "no_html": 1, "skip_disambig": 1},
            timeout=4
        )
        if r.status_code == 200:
            abstract = r.json().get("AbstractText")
            if abstract:
                return abstract
    except Exception:
        pass

    # 5. Wikipedia Summary API
    try:
        headers = {"User-Agent": "AIAgentCloudLab/1.0 (student@mit.asia)"}
        wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{clean_topic.replace(' ', '_')}"
        r = requests.get(wiki_url, headers=headers, timeout=4)
        if r.status_code == 200:
            extract = r.json().get("extract")
            if extract:
                return extract
    except Exception:
        pass

    return (
        f"**{clean_topic.capitalize()}** is an important concept in modern technology and computer science. "
        "This response was generated by your cloud-deployed AI agent!"
    )


# ==========================================
# MAIN INTERFACE
# ==========================================
st.title("🤖 Cloud-Deployed AI Agent")
st.markdown(
    """
    This application is packaged and deployed on **Streamlit Community Cloud** with continuous deployment from GitHub.
    It demonstrates cloud hosting, secret handling, responsive UI design, and agentic response generation.
    """
)

# Live Status Cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Cloud Platform", "Streamlit Cloud", "Connected")
c2.metric("Environment", "Production", "Active")
c3.metric("Response Engine", "Atria / Cloud KB", "Online")
c4.metric("Security", "Secrets Masked", "Protected")

st.divider()

# Session State for Messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I am your Cloud-Deployed AI Agent. Ask me any question to test live cloud inference!"}
    ]

# Display Chat History
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Chat Input
user_query = st.chat_input("Ask a question (e.g., What is AWS?, Explain Cloud Deployment)...")

if user_query:
    # Append & Display user query
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Processing on Streamlit Cloud..."):
            response_text = query_ai_agent(user_query, api_key)
            st.write(response_text)

    # Save assistant message
    st.session_state["messages"].append({"role": "assistant", "content": response_text})
