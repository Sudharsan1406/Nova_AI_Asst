import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_response(messages, model_name):
    """
    Returns a streaming response from Groq.
    """

    stream = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=True
    )

    return stream