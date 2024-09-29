""" Command to perform code scanning """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_pilot_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def scan(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File containing code to scan for vulnerabilities."),
    ],
) -> None:
    """
    Scan the provided code for security vulnerabilities.

    Args:
        code (typer.FileText): The file containing code to be scanned.
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                SYSTEM_MESSAGE,
                {
                    "role": "user",
                    "content": f"Perform a code scan to identify security vulnerabilities:\n{code.read()}",
                },
            ],
            max_tokens=1024,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
