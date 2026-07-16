import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


# ===========================
# Database Connection
# ===========================

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


# ===========================
# User Functions
# ===========================

def create_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO users (username)
    VALUES (%s)
    """

    cursor.execute(query, (username,))
    conn.commit()

    cursor.close()
    conn.close()


def get_user(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM users
    WHERE username = %s
    """

    cursor.execute(query, (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


# ===========================
# Conversation Functions
# ===========================

def create_conversation(user_id, title="New Chat"):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO conversations (user_id, title)
    VALUES (%s, %s)
    """

    cursor.execute(query, (user_id, title))
    conn.commit()

    conversation_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return conversation_id


def get_conversations(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM conversations
    WHERE user_id=%s
    ORDER BY created_at DESC
    """

    cursor.execute(query, (user_id,))
    conversations = cursor.fetchall()

    cursor.close()
    conn.close()

    return conversations


def get_conversation(conversation_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM conversations
    WHERE id=%s
    """

    cursor.execute(query, (conversation_id,))
    conversation = cursor.fetchone()

    cursor.close()
    conn.close()

    return conversation


def update_conversation_title(conversation_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE conversations
    SET title=%s
    WHERE id=%s
    """

    cursor.execute(query, (title, conversation_id))
    conn.commit()

    cursor.close()
    conn.close()


def delete_conversation(conversation_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM conversations
    WHERE id=%s
    """

    cursor.execute(query, (conversation_id,))
    conn.commit()

    cursor.close()
    conn.close()


# ===========================
# Message Functions
# ===========================

def save_message(conversation_id, role, message):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO messages
    (conversation_id, role, message)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (conversation_id, role, message)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_messages(conversation_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT role, message
    FROM messages
    WHERE conversation_id=%s
    ORDER BY id ASC
    """

    cursor.execute(query, (conversation_id,))
    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return messages


# ===========================
# Memory Functions
# ===========================

def save_memory(user_id, key, value):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO memory
    (user_id, memory_key, memory_value)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (user_id, key, value)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_memory(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT memory_key, memory_value
    FROM memory
    WHERE user_id=%s
    """

    cursor.execute(query, (user_id,))
    memory = cursor.fetchall()

    cursor.close()
    conn.close()

    return memory


def update_memory(user_id, key, value):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE memory
    SET memory_value=%s
    WHERE user_id=%s
    AND memory_key=%s
    """

    cursor.execute(
        query,
        (value, user_id, key)
    )

    conn.commit()

    cursor.close()
    conn.close()


# ===========================
# Utility
# ===========================

def close_connection(conn):
    if conn.is_connected():
        conn.close()