""" Command to generate shell commands """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def ai(
    prompt: Annotated[
        str, typer.Argument(help="Natural language prompt for command generation.")
    ],
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
) -> None:
    """
    Generate shell commands based on a natural language prompt.

    Args:
        prompt (str): The natural language prompt from which to generate a command.
        code: (Optional[str]): Code file to include in the prompt.
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
            max_tokens=1024,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
