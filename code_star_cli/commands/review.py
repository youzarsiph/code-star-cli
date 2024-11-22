""" Perform code reviews using CodeStar """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, create_panel


def review(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File containing code to review for quality improvements."),
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
    Perform code reviews to analyze code quality and adherence to best practices,
    to provide developers with suggestions for improvement

    Examples:
    ```shell
    code-star review code.py
    code-star review code.py -o code-review.md
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
