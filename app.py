import streamlit as st

from components.login import show_login
from components.sidebar import show_sidebar
from components.chat import show_chat

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Nova AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Initialize Session
# -----------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = None

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Login
# -----------------------------

logged_in = show_login()

if not logged_in:
    st.stop()

# -----------------------------
# Sidebar
# -----------------------------

model_name = show_sidebar()

# -----------------------------
# Main Header
# -----------------------------

st.title("🤖 Nova AI Assistant")

st.caption(
    "Powered by Groq • Llama 3 • Streamlit • MySQL"
)

# -----------------------------
# Chat Window
# -----------------------------

show_chat(model_name)