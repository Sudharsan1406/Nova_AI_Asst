import re

# ---------------------------
# Input Validation
# ---------------------------

MAX_INPUT_LENGTH = 2000


def validate_input(text):
    """
    Validate user input before sending to the LLM.
    Returns:
        (True, "") if valid
        (False, error_message) if invalid
    """

    text = text.strip()

    # Empty Input
    if not text:
        return False, "Please enter a message."

    # Maximum Length
    if len(text) > MAX_INPUT_LENGTH:
        return False, f"Maximum {MAX_INPUT_LENGTH} characters allowed."

    # SQL Injection Check
    sql_patterns = [
        r"drop\s+table",
        r"truncate\s+table",
        r"delete\s+from",
        r"insert\s+into",
        r"update\s+\w+\s+set",
        r"alter\s+table"
    ]

    for pattern in sql_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return False, "Potential SQL command detected."

    return True, ""


# ---------------------------
# Generate Chat Title
# ---------------------------

def generate_title(message):
    """
    Generate a conversation title
    from the user's first message.
    """

    message = message.strip()

    words = message.split()

    title = " ".join(words[:6])

    if len(words) > 6:
        title += "..."

    return title


# ---------------------------
# Convert DB Messages
# ---------------------------

def format_messages(db_messages):
    """
    Convert database messages into
    LLM message format.
    """

    formatted = []

    for msg in db_messages:

        formatted.append(
            {
                "role": msg["role"],
                "content": msg["message"]
            }
        )

    return formatted