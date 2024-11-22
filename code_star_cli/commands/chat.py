""" Chat with CodeStar """

import json
from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_star_cli import CHAT_LLM, SYSTEM_MESSAGE, create_panel


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
    Engage in a chat session with CodeStar.

    Examples:
    ```shell
    # Star chatting
    code-star chat --

    # Export chat history
    code-star chat -e chat_history.json

    # Import chat history
    code-star chat -h chat_history.json

    # Import chat history then export it after the chat session
    code-star chat -h chat_history.json -e chat_history.json
    ```
    """

    client = InferenceClient(CHAT_LLM)

    messages = [SYSTEM_MESSAGE]

    if history:
        messages = json.load(history)

    print(
        create_panel(
            "CodeStar",
            "Hi, how I can assist you today?",
            "Type 'exit' or 'quit' to end the chat.",
        )
    )

    while True:
        message = typer.prompt(
            typer.style("You", fg=typer.colors.MAGENTA, bold=True),
            type=str,
        )

        if message.lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": message})

        try:
            response = client.chat_completion(messages=messages, max_tokens=max_tokens)
            llm_message = str(response.choices[0].message.content)

            messages.append({"role": "assistant", "content": llm_message})

            print(create_panel("CodeStar", llm_message))

        except Exception as error:
            print(f"[bold red]Error[/bold red]: {error}")
            break

    export_requested = False

    if not export:
        export_requested: bool = typer.prompt(
            "CodeStar: Do you want to save this chat?",
            type=bool,
            default=False,
            show_default=True,
            prompt_suffix="",
        )

        if export_requested:
            file_name: str = typer.prompt(
                "Enter a file name to save the chat history",
                type=str,
                default="chat-history.json",
            )

            # Ensure the file type is JSON
            file_name = (
                file_name if file_name.endswith(".json") else file_name + ".json"
            )

            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(messages, file, indent=2)

    if export:
        json.dump(messages, export, indent=2)
