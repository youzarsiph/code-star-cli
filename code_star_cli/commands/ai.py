""" Command to generate shell commands """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_pilot_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def ai(
    prompt: Annotated[
        str, typer.Argument(help="Natural language prompt for command generation.")
    ],
) -> None:
    """
    Generate shell commands based on a natural language prompt.

    Args:
        prompt (str): The natural language prompt from which to generate a command.
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[SYSTEM_MESSAGE, {"role": "user", "content": prompt}],
            max_tokens=1024,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
