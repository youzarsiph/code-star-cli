"""CodeStar CLI - An advanced AI-powered coding assistant."""

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
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are CodeStar, an advanced coding assistant powered by StarCoder 2,"
    " a state-of-the-art Large Language Model for Code (Code LLM) trained on over 600 "
    "programming languages from a diverse set of permissively licensed data, including "
    "GitHub code, Arxiv, and Wikipedia. CodeStar is specifically optimized for enhanced "
    "performance in coding tasks.",
}

# CLI
code_star = typer.Typer(
    name="code-star",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="CodeStar CLI. CodeStar is an advanced AI-powered coding assistant.",
)


# Syntax Highlighting
def print_highlighted(code: str) -> None:
    """
    Highlight and print the provided code.

    Args:
        code (str): The code to be highlighted and printed.
    """

    console = Console()
    highlighted_code = Syntax(
        code,
        "markdown",
        theme="github-dark",
        code_width=120,
        word_wrap=True,
        background_color="default",
    )

    console.print(highlighted_code)


@code_star.command()
def ai(
    prompt: Annotated[
        str, typer.Argument(help="Natural language prompt for command generation.")
    ]
) -> None:
    """
    Generate shell commands based on a natural language prompt.

    Args:
        prompt (str): The natural language prompt from which to generate a command.
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[SYSTEM_MESSAGE, {"role": "user", "content": prompt}],
            max_tokens=1024,
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

    print(
        "CodeStar Chat\n"
        "Type [bold red]exit[/bold red] or [bold red]quit[/bold red] to exit\n"
    )

    while True:
        message = typer.prompt(
            typer.style("You", fg=typer.colors.GREEN, bold=True),
            type=str,
        )

        if message in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": message})

        try:
            response = client.chat_completion(messages=messages, max_tokens=2048)
            llm_message = str(response.choices[0].message.content)

            messages.append({"role": "assistant", "content": llm_message})

            print("[bold blue]CodeStar[/bold blue]:")
            print_highlighted(llm_message)

        except Exception as error:
            print(f"[bold red]Error[/bold red]: {error}")
            break

    if export:
        json.dump(messages, export, indent=2)


@code_star.command()
def completions(
    code: Annotated[str, typer.Argument(help="Code snippet to complete.")]
) -> None:
    """
    Generate code completions based on the provided code snippet.

    Args:
        code (str): The code to complete.
    """

    client = InferenceClient(COMPLETION_LLM)

    try:
        generated_code = client.text_generation(code, max_new_tokens=1024)

        print("[bold blue]CodeStar[/bold blue]:")
        print_highlighted(code + generated_code)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")


@code_star.command()
def enhance(
    code: Annotated[
        typer.FileText,
        typer.Argument(
            help="File containing code to enhance for quality improvements."
        ),
    ]
) -> None:
    """
    Improve code quality by applying best practices.

    Args:
        code (typer.FileText): The file containing code to be enhanced.
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                SYSTEM_MESSAGE,
                {
                    "role": "user",
                    "content": "Apply best practices, enhancements, and industry standards to the provided "
                    f"code to make it more efficient, secure, and maintainable:\n{code.read()}",
                },
            ],
            max_tokens=2048,
        )

        print("[bold blue]CodeStar[/bold blue]:")
        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")


@code_star.command()
def scan(
    code: Annotated[
        typer.FileText,
        typer.Argument(help="File containing code to scan for vulnerabilities."),
    ]
) -> None:
    """
    Scan the provided code for security vulnerabilities.

    Args:
        code (typer.FileText): The file containing code to be scanned.
    """

    client = InferenceClient(CHAT_LLM)

    try:
        response = client.chat_completion(
            messages=[
                SYSTEM_MESSAGE,
                {
                    "role": "user",
                    "content": f"Perform a code scan to identify security vulnerabilities:\n{code.read()}",
                },
            ],
            max_tokens=1024,
        )

        print("[bold blue]CodeStar[/bold blue]:")
        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")


if __name__ == "__main__":
    # Load environment variables
    load_dotenv(override=True)

    code_star()
