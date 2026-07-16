import streamlit as st

from database import (
    create_user,
    get_user
)

from memory import remember_login_name


def login():

    st.title("🤖 Nova AI Assistant")
    st.subheader("Login")

    username = st.text_input(
        "Username",
        placeholder="Enter your username"
    )

    login_btn = st.button(
    "Login",
    use_container_width=True
    )


    # ---------------- Login ---------------- #

    if login_btn:

        username = username.strip()

        if username == "":
            st.warning("Username cannot be empty.")
            st.stop()

        create_user(username)

        user = get_user(username)

        st.session_state.user = user
        st.session_state.user_id = user["id"]
        st.session_state.username = user["username"]

        # Save login name into memory
        remember_login_name(
            user["id"],
            user["username"]
        )

        st.success(f"Welcome {user['username']} 👋")

        st.rerun()


def logout():

    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()


def is_logged_in():

    return st.session_state.get("username") is not None