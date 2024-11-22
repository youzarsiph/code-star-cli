""" Natural language interactions like command generation """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, create_panel


def ai(
    prompt: Annotated[str, typer.Argument(help="Natural language prompt.")],
    code: Annotated[
        Optional[typer.FileText],
        typer.Option(
            "--code",
            "-c",
            exists=True,
            help="Code file to include in the prompt.",
            encoding="utf-8",
        ),
    ] = None,
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
    Interact with CodeStar using natural language.

    Examples:
    ```shell
    code-star ai "Generate a function to calculate the area of a circle"
    code-star ai -c code.py "Explain the code"
    code-star ai -o output.md "How to install HuggingFace Transformers?"
    ```
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                SYSTEM_MESSAGE,
                {
                    "role": "user",
                    "content": (
                        f"{prompt}:\n```\n{code.read()}\n```" if code else prompt
                    ),
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
