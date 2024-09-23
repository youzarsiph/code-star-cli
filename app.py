""" CodeStar CLI """

import json
from typing import Annotated, Dict, List, Literal, Optional
import typer
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from rich import print
from rich.console import Console
from rich.syntax import Syntax


# Constants
CHAT_LLM = "HuggingFaceH4/starchat2-15b-v0.1"
COMPLETION_LLM = "bigcode/starcoder2-15b"

# CLI
code_star = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="CodeStar CLI. CodeStar is an advanced AI-powered coding assistant.",
)


# Syntax highlight
def print_highlighted(code: str) -> None:
    """Highlight given code then prints it"""

    console = Console()
    highlighted_code = Syntax(
        code,
        "markdown",
        theme="github-dark",
        code_width=120,
        word_wrap=True,
        background_color="default",
        indent_guides=True,
        padding=1,
    )

    console.print(highlighted_code)


@code_star.command()
def ai(prompt: Annotated[str, typer.Argument(help="Natural language prompt")]) -> None:
    """
    Generate shell commands using natural language.

    \b
    Example:
    ```bash
    code-star ai 'How to navigate the file system in terminal'
    ```
    """

    # HF Inference client
    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are CodeStar, an advanced coding assistant powered by StarCoder 2,"
                    " a state-of-the-art Large Language Model for Code (Code LLM) trained on over 600 "
                    "programming languages from a diverse set of permissively licensed data, including "
                    "GitHub code, Arxiv, and Wikipedia. CodeStar is specifically optimized for enhanced "
                    "performance in coding tasks.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=512,
        )

        print("[bold blue]CodeStar[/bold blue]:")
        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")


@code_star.command()
def chat(
    export: Annotated[
        Optional[typer.FileTextWrite],
        typer.Option(
            "--export",
            "-e",
            help="File to export chat history",
            encoding="utf-8",
        ),
    ] = None,
    history: Annotated[
        Optional[typer.FileText],
        typer.Option(
            "--history",
            "-h",
            help="File to import chat history",
            encoding="utf-8",
        ),
    ] = None,
) -> None:
    """
    Chat with CodeStar

    \b
    Examples:
    ```bash
    code-star chat
    # Export chat history
    code-star chat -e chat_history.json
    # Import chat history
    code-star chat -h chat_history.json
    ```
    """

    # HF Inference client
    client = InferenceClient(CHAT_LLM)

    # Chat history
    messages: List[Dict[Literal["role", "content"], str]] = [
        {
            "role": "system",
            "content": "You are CodeStar, an advanced coding assistant powered by StarCoder 2,"
            " a state-of-the-art Large Language Model for Code (Code LLM) trained on over 600 "
            "programming languages from a diverse set of permissively licensed data, including "
            "GitHub code, Arxiv, and Wikipedia. CodeStar is specifically optimized for enhanced "
            "performance in coding tasks.",
        }
    ]

    # Import chat history if provided
    if history:
        messages = json.load(history)

    # Help message
    print(
        "CodeStar Chat\n"
        "Type [bold red]exit[/bold red] or [bold red]quit[/bold red] to exit\n"
    )

    # Chat loop
    while True:
        # User message
        message = typer.prompt(
            typer.style("You", fg=typer.colors.GREEN, bold=True),
            type=str,
        )

        if message in ("exit", "quit"):
            break

        # Add to chat history
        messages.append({"role": "user", "content": message})

        try:
            # LLM message
            response = client.chat_completion(messages=messages, max_tokens=2048)
            llm_message = str(response.choices[0].message.content)

            # Add to chat history
            messages.append({"role": "assistant", "content": llm_message})

            print("[bold blue]CodeStar[/bold blue]:")
            print_highlighted(llm_message)

        except Exception as error:
            print(f"[bold red]Error[/bold red]: {error}")

            # Exit chat loop
            break

    # Export chat history
    if export:
        json.dump(messages, export, indent=2)


@code_star.command()
def completions(code: Annotated[str, typer.Argument(help="Code to complete")]) -> None:
    """
    Get code completions from CodeStar

    \b
    Example:
    ```bash
    code-pilot completions 'fn read_file(path: PathBuf) -> Result<String, Error> {'
    ```
    """

    # HF Inference client
    client = InferenceClient(COMPLETION_LLM)

    try:
        generated_code = client.text_generation(code, max_new_tokens=128)

        print("[bold blue]CodeStar[/bold blue]:")
        print_highlighted(code + generated_code)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")


@code_star.command()
def scan(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File to scan for vulnerabilities"),
    ]
) -> None:
    """
    Perform code scans with CodeStar for vulnerabilities

    \b
    Example:
    ```bash
    code-pilot scan code.py
    ```
    """

    # HF Inference client
    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are CodeStar, an advanced coding assistant powered by StarCoder 2,"
                    " a state-of-the-art Large Language Model for Code (Code LLM) trained on over 600 "
                    "programming languages from a diverse set of permissively licensed data, including "
                    "GitHub code, Arxiv, and Wikipedia. CodeStar is specifically optimized for enhanced "
                    "performance in coding tasks.",
                },
                {
                    "role": "user",
                    "content": f"Perform a code scan to identify security vulnerabilities :\n{code.read()}",
                },
            ],
            max_tokens=512,
        )

        print("[bold blue]CodeStar[/bold blue]:")
        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")


if __name__ == "__main__":
    # Load secrets
    load_dotenv(override=True)

    code_star()
