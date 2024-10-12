""" Generate code completions """

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
    Generate code completions based on the provided code snippet.

    Args:
        code (str): The code to complete.
        language (str, optional): The programming language of the code snippet. Defaults to 'python'.

    Examples:
    ```shell
    code-star completions 'def hello_world():'
    code-star completions -l python 'def hello_world():'
    code-star completions -o code-completions.md 'def hello_world():'
    ```
    """

    client = InferenceClient(COMPLETION_LLM)

    try:
        response = client.text_generation(
            f"```{language if language else ''}\n{code}",
            max_new_tokens=256,
        )

        if output:
            with output as file:
                file.write(f"```{language if language else ''}\n{code + response}")

            print(f"Output [bold green]saved[/bold green] to {output.name}.")

        else:
            print_highlighted(f"```{language if language else ''}\n{code + response}")

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
