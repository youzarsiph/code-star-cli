""" Generate documentation for code """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, create_panel


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
    max_tokens: Annotated[
        Optional[int],
        typer.Option(
            "--max-tokens",
            "-t",
            help="Maximum number of tokens allowed in the response.",
        ),
    ] = 2048,
) -> None:
    """
    Add documentation to the provided code.

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
            max_tokens=max_tokens,
        )

        if output:
            with output as file:
                file.write(str(response.choices[0].message.content))

            print(f"Output [bold green]saved[/bold green] to {output.name}.")

        else:
            print(create_panel("CodeStar", str(response.choices[0].message.content)))

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
