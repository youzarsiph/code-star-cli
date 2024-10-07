""" Command to perform code scanning """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def scan(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File containing code to scan for vulnerabilities."),
    ],
) -> None:
    """
    Scan the provided code for security vulnerabilities to provide suggestions on how to improve it.

    Args:
        code (typer.FileText): The file containing code to be scanned.

    Examples:
    ```shell
    code-star scan code.py
    ```
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                SYSTEM_MESSAGE,
                {
                    "role": "user",
                    "content": "As a an expert software engineer and cybersecurity engineer "
                    "that puts code into production in large scale systems. Your job is to ensure "
                    "that code runs effectively, quickly, at scale, and securely. Please perform a "
                    "code scan to identify potential security vulnerabilities in the provided code:"
                    f"\n{code.read()}",
                },
            ],
            max_tokens=1024,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
