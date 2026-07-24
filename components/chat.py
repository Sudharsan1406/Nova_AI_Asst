import streamlit as st
import time

from chatbot import get_response
from prompt import SYSTEM_PROMPT

from database import (
    create_conversation,
    save_message,
    get_messages,
    update_conversation_title
)

from utils import (
    validate_input,
    generate_title,
    format_messages
)

from memory import (
    extract_memory,
    build_memory_prompt
)


def show_chat(model_name):

    # ---------------- Guest ---------------- #

    is_guest = st.session_state.get("user_id") is None

    # ---------------- Load Conversation ---------------- #

    if not is_guest:

        conversation_id = st.session_state.get("conversation_id")

        if conversation_id:

            if (
                st.session_state.get("loaded_conversation")
                != conversation_id
            ):

                db_messages = get_messages(conversation_id)

                st.session_state.messages = format_messages(
                    db_messages
                )

                st.session_state.loaded_conversation = conversation_id

    # ---------------- Display Messages ---------------- #

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            st.markdown(msg["content"])

    # ---------------- Chat Input ---------------- #

    prompt = st.chat_input("Ask anything...")

    if not prompt:
        return

    # ---------------- Validation ---------------- #

    valid, error = validate_input(prompt)

    if not valid:

        st.warning(error)

        return

    # ---------------- Create Conversation ---------------- #

    if (
        not is_guest
        and
        st.session_state.get("conversation_id") is None
    ):

        conversation_id = create_conversation(
            st.session_state.user_id
        )

        st.session_state.conversation_id = conversation_id

    # ---------------- User Message ---------------- #

    with st.chat_message("user"):

        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # ---------------- Save User ---------------- #

    if not is_guest:

        save_message(
            st.session_state.conversation_id,
            "user",
            prompt
        )

        if len(st.session_state.messages) == 1:

            update_conversation_title(
                st.session_state.conversation_id,
                generate_title(prompt)
            )

    # ---------------- Memory ---------------- #

    if not is_guest:

        extract_memory(
            st.session_state.user_id,
            prompt
        )

        memory_prompt = build_memory_prompt(
            st.session_state.user_id
        )

    else:

        memory_prompt = ""

    # ---------------- Build Prompt ---------------- #

    llm_messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT + "\n\n" + memory_prompt
        }

    ]

    llm_messages.extend(st.session_state.messages)

    # ---------------- AI Response ---------------- #

    start = time.time()

    reply = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        try:

            stream = get_response(
                llm_messages,
                model_name
            )

            for chunk in stream:

                content = chunk.choices[0].delta.content

                if content:

                    reply += content

                    placeholder.markdown(
                        reply + "▌"
                    )

            placeholder.markdown(reply)

        except Exception as e:

            st.error(e)

            return

    end = time.time()

    st.caption(
        f"⏱ Response Time: {round(end-start,2)} sec"
    )

    # ---------------- Save Assistant ---------------- #

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    if not is_guest:

        save_message(
            st.session_state.conversation_id,
            "assistant",
            reply
        )