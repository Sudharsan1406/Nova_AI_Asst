import streamlit as st
from auth import login

def show_login():

    if st.session_state.get("user_id") is not None:
        return True

    login()

    return False