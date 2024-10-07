""" Command to improve code quality """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def enhance(
    code: Annotated[
        typer.FileText,
        typer.Argument(
            help="File containing code to enhance for quality improvements."
        ),
    ],
) -> None:
    """
    Improve code quality by applying best practices and enhancements suggested by CodeStar.

    Args:
        code (typer.FileText): The file containing code to be enhanced.

    Examples:
    ```shell
    code-star enhance code.py
    ```
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                SYSTEM_MESSAGE,
                {
                    "role": "user",
                    "content": "As a an expert software engineer and site reliability engineer "
                    "that puts code into production in large scale systems. Your job is to ensure "
                    "that code runs effectively, quickly, at scale, and securely. Please profile it, "
                    "and find any issues that need to be fixed or updated. Also apply best practices, "
                    "enhancements, and industry standards to the provided code to make it more efficient, "
                    f"secure, and maintainable:\n{code.read()}",
                },
            ],
            max_tokens=2048,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
