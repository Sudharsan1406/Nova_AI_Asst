import streamlit as st

from auth import logout
from database import (
    create_conversation,
    get_conversations,
    delete_conversation
)


def show_sidebar():

    with st.sidebar:

        st.title("🤖 Nova AI")

        username = st.session_state.get("username", "Guest")
        st.markdown(f"### 👤 {username}")

        st.markdown("---")

        st.selectbox(
            "Choose Model",
            [
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant"
            ],
            key="model_name"
        )

        st.markdown("---")

        is_guest = st.session_state.get("user_id") is None

        # ---------------- New Chat ---------------- #

        if st.button(
            "➕ New Chat",
            use_container_width=True
        ):

            st.session_state.messages = []
            st.session_state.loaded_conversation = None

            if not is_guest:

                conversation_id = create_conversation(
                    st.session_state.user_id
                )

                st.session_state.conversation_id = conversation_id

            else:

                st.session_state.conversation_id = None

            st.rerun()

        st.markdown("### 💬 Conversations")

        if is_guest:

            st.info("Guest Mode\n\nHistory is not saved.")

        else:

            conversations = get_conversations(
                st.session_state.user_id
            )

            if len(conversations) == 0:

                st.info("No conversations yet.")

            else:

                for conv in conversations:

                    col1, col2 = st.columns([5, 1])

                    with col1:

                        if st.button(
                            conv["title"],
                            key=f"conv_{conv['id']}",
                            use_container_width=True
                        ):

                            st.session_state.conversation_id = conv["id"]
                            st.session_state.loaded_conversation = None
                            st.rerun()

                    with col2:

                        if st.button(
                            "🗑",
                            key=f"delete_{conv['id']}"
                        ):

                            delete_conversation(conv["id"])

                            if (
                                st.session_state.get("conversation_id")
                                == conv["id"]
                            ):

                                st.session_state.conversation_id = None
                                st.session_state.messages = []
                                st.session_state.loaded_conversation = None

                            st.rerun()

        st.markdown("---")

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            logout()

    return st.session_state.model_name