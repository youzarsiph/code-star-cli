""" Command to perform code reviews using CodeStar """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def review(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File containing code to review for quality improvements."),
    ],
) -> None:
    """
    Perform code reviews to analyze code quality and adherence to best practices,
    to provide developers with suggestions for improvement

    Args:
        code (typer.FileText): The file containing code to be reviewed.

    Examples:
    ```shell
    code-star review code.py
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
                    "that code runs effectively, quickly, at scale, and securely. Please review and "
                    "analyze code quality and adherence to best practices, providing developers with "
                    f"suggestions for improvement:\n{code.read()}",
                },
            ],
            max_tokens=2048,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
