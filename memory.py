import re

from database import (
    get_memory,
    save_memory,
    update_memory
)


PATTERNS = {

    "name": [
        r"my name is (.+)",
        r"i am (.+)",
        r"i'm (.+)"
    ],

    "city": [
        r"i live in (.+)",
        r"i am from (.+)"
    ],

    "favorite_color": [
        r"my favorite color is (.+)"
    ],

    "favorite_language": [
        r"my favorite language is (.+)"
    ]
}


def remember_login_name(user_id, username):

    if user_id is None:
        return

    memory = get_memory(user_id)

    for item in memory:

        if item["memory_key"] == "name":

            update_memory(
                user_id,
                "name",
                username
            )

            return

    save_memory(
        user_id,
        "name",
        username
    )


def extract_memory(user_id, message):

    if user_id is None:
        return

    message = message.lower()

    for key, patterns in PATTERNS.items():

        for pattern in patterns:

            match = re.search(
                pattern,
                message,
                re.IGNORECASE
            )

            if match:

                value = match.group(1).strip()

                memory = get_memory(user_id)

                exists = False

                for item in memory:

                    if item["memory_key"] == key:

                        update_memory(
                            user_id,
                            key,
                            value
                        )

                        exists = True
                        break

                if not exists:

                    save_memory(
                        user_id,
                        key,
                        value
                    )

                return


def build_memory_prompt(user_id):

    if user_id is None:
        return ""

    memory = get_memory(user_id)

    if len(memory) == 0:
        return ""

    prompt = (
        "The following facts are permanently known about the user.\n"
        "Use them in every conversation naturally.\n\n"
    )

    for item in memory:

        prompt += (
            f"{item['memory_key']}: "
            f"{item['memory_value']}\n"
        )

    return prompt