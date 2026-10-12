"""
Practical 9: AI Agent
Created by Suyash Singh
Entrypoint for Streamlit: streamlit run app.py
"""

import os
import re
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="AI Agent | Suyash Singh",
    page_icon="🤖",
    layout="centered"
)

# Minimal custom styling
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# CREDENTIALS
# ==========================================
DEFAULT_ATRIA_KEY = "atr_n7FB_XvmYAJ0P4cDFL1b46Ix7P-8w3_B"

api_key = None
try:
    if hasattr(st, "secrets"):
        api_key = st.secrets.get("ATRIA_API_KEY", None) or st.secrets.get("OPENAI_API_KEY", None)
except Exception:
    api_key = None

if not api_key:
    api_key = os.getenv("ATRIA_API_KEY") or os.getenv("OPENAI_API_KEY") or DEFAULT_ATRIA_KEY


# ==========================================
# CREATOR & AI RESPONSE ENGINE
# ==========================================
def is_creator_query(text: str) -> bool:
    """Checks if the user is asking about the creator/maker."""
    clean = re.sub(r"[^a-zA-Z\s]", "", text.lower()).strip()
    creator_patterns = [
        "who made you",
        "who created you",
        "who built you",
        "who developed you",
        "who is your creator",
        "who is your maker",
        "who is your developer",
        "who programmed you",
        "who designed you",
        "who is your author",
        "who are you made by",
        "who made this",
        "who made this agent",
        "who made this app",
        "whose ai are you",
        "who is your owner"
    ]
    return any(p in clean for p in creator_patterns)


def query_ai_agent(prompt: str, chat_history: list = None) -> str:
    """Answers any question with strict attribution to Suyash Singh."""
    clean_p = prompt.strip()

    # 1. Creator check - always returns Suyash Singh
    if is_creator_query(clean_p):
        return "I was created and developed by **Suyash Singh**."

    # 2. Basic Greetings
    if clean_p.lower() in ["hi", "hello", "hey", "hola"]:
        return "Hello! How can I help you today?"

    # 3. Arithmetic tool
    clean_math = re.sub(r"[^0-9+\-*/().% ]", "", clean_p).strip()
    if clean_math and any(op in clean_math for op in ["+", "-", "*", "/"]) and any(c.isdigit() for c in clean_math):
        try:
            res = eval(clean_math, {"__builtins__": {}}, {})
            return f"**Result:** `{clean_math} = {res}`"
        except Exception:
            pass

    # 4. Atria ASI Model with custom system instruction
    if api_key:
        try:
            url = "https://api.atria-asi.ai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            system_instruction = (
                "You are a helpful, smart, and direct AI Assistant created and developed by Suyash Singh. "
                "Answer any question the user asks clearly, concisely, and factually. "
                "If asked about who made you or created you, always state clearly that you were created by Suyash Singh."
            )

            messages = [{"role": "system", "content": system_instruction}]

            if chat_history:
                for msg in chat_history[-6:]:
                    if msg.get("role") in ["user", "assistant"]:
                        messages.append({"role": msg["role"], "content": msg["content"]})

            messages.append({"role": "user", "content": clean_p})

            data = {
                "model": "Atria-Dawn-Preview",
                "messages": messages
            }

            res = requests.post(url, headers=headers, json=data, timeout=60)
            if res.status_code == 200:
                answer = res.json()["choices"][0]["message"]["content"]
                if answer and len(answer.strip()) > 0:
                    return answer.strip()
        except Exception:
            pass

    # 5. Wikipedia Search Fallback (for any general query)
    try:
        headers = {"User-Agent": "AIAgentCloud/1.0 (student@mit.asia)"}
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": clean_p,
            "format": "json",
            "utf8": 1
        }
        sr = requests.get("https://en.wikipedia.org/w/api.php", headers=headers, params=search_params, timeout=5)
        if sr.status_code == 200:
            data = sr.json()
            search_results = data.get("query", {}).get("search", [])
            if search_results:
                best_title = search_results[0]["title"]
                summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{best_title.replace(' ', '_')}"
                r_summary = requests.get(summary_url, headers=headers, timeout=5)
                if r_summary.status_code == 200:
                    extract = r_summary.json().get("extract")
                    if extract:
                        return f"**{best_title}:**\n\n{extract}"
    except Exception:
        pass

    return f"I received your question: '{clean_p}'. Feel free to ask more details!"


# ==========================================
# MINIMAL SIDEBAR
# ==========================================
with st.sidebar:
    st.title("🤖 AI Agent")
    st.caption("Developed by **Suyash Singh**")
    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hello! How can I help you today?"}
        ]
        st.rerun()


# ==========================================
# CLEAN MINIMAL UI
# ==========================================
st.title("🤖 AI Agent")
st.caption("Ask anything • Developed by Suyash Singh")

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Display messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
user_query = st.chat_input("Type your message here...")

if user_query:
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_text = query_ai_agent(user_query, st.session_state["messages"])
            st.markdown(response_text)

    st.session_state["messages"].append({"role": "assistant", "content": response_text})
