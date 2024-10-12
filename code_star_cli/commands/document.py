""" Generate documentation for code """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def document(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File containing code to add documentation."),
    ],
    output: Annotated[
        Optional[typer.FileTextWrite],
        typer.Option(
            "--output",
            "-o",
            help="Output file to write the response to.",
            encoding="utf-8",
        ),
    ] = None,
) -> None:
    """
    Add documentation to the provided code.

    Args:
        code (typer.FileText): The file containing code to be documented.

    Examples:
    ```shell
    code-star document code.py
    code-star document code.py -o code-docs.md
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
                    "that code runs effectively, quickly, at scale, and securely. Please document the "
                    "provided code, including any potential issues or improvements that could be made, "
                    "and provide the updated code with the documentation included. The documentation "
                    "should include docstrings, comments, and any other relevant information that could "
                    "help developers better understand the code's purpose, functionality, and behavior:\n"
                    f"{code.read()}",
                },
            ],
            max_tokens=2048,
        )

        if output:
            with output as file:
                file.write(response.choices[0].message.content)

            print(f"Output [bold green]saved[/bold green] to {output.name}.")

        else:
            print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
