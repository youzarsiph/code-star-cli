""" Command to generate shell commands """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import COMPLETION_LLM, print_highlighted


def completions(
    code: Annotated[str, typer.Argument(help="Code snippet to complete.")],
    language: Annotated[
        Optional[str],
        typer.Option(
            "--lang",
            "-l",
            help="Programming language of the code snippet.",
        ),
    ] = None,
) -> None:
    """
    Generate code completions based on the provided code snippet.

    Args:
        code (str): The code to complete.
        language (str, optional): The programming language of the code snippet. Defaults to 'python'.

    Examples:
    ```shell
    code-star completions 'def hello_world():'
    ```
    """

    client = InferenceClient(COMPLETION_LLM)

    try:
        response = client.text_generation(
            f"```{language if language else ''}\n{code}",
            max_new_tokens=256,
        )

        print_highlighted(f"```{language if language else ''}\n{code + response}")

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
