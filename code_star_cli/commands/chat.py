""" Command to chat with CodeStar """

import json
from typing import Annotated, Dict, List, Literal, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_pilot_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def chat(
    export: Annotated[
        Optional[typer.FileTextWrite],
        typer.Option(
            "--export",
            "-e",
            help="File to export chat history.",
            encoding="utf-8",
        ),
    ] = None,
    history: Annotated[
        Optional[typer.FileText],
        typer.Option(
            "--history",
            "-h",
            help="File to import previous chat history.",
            encoding="utf-8",
        ),
    ] = None,
) -> None:
    """
    Engage in a chat session with CodeStar.

    Args:
        export (Optional[typer.FileTextWrite]): Optional file to save chat history.
        history (Optional[typer.FileText]): Optional file to load previous chat history.
    """

    client = InferenceClient(CHAT_LLM)

    messages: List[Dict[Literal["role", "content"], str]] = [SYSTEM_MESSAGE]

    if history:
        messages = json.load(history)

    print_highlighted("[bold red]exit[/bold red] or [bold red]quit[/bold red]")

    while True:
        message = typer.prompt(
            typer.style("You", fg=typer.colors.MAGENTA, bold=True),
            type=str,
        )

        if message.lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": message})

        try:
            response = client.chat_completion(messages=messages, max_tokens=2048)
            llm_message = str(response.choices[0].message.content)

            messages.append({"role": "assistant", "content": llm_message})

            print_highlighted(llm_message)

        except Exception as error:
            print(f"[bold red]Error[/bold red]: {error}")
            break

    if export:
        json.dump(messages, export, indent=2)
