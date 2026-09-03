
import os
from openai import OpenAI


def ask_llm(prompt):
    """
    Send a prompt to the LLM and return its response.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return (
            "LLM explanation unavailable. "
            "Please configure OPENAI_API_KEY."
        )

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text

    except Exception:
        return (
            "LLM explanation is currently unavailable. "
            "The security analysis and automatic fix were still completed."
        )
