""" CodeStar CLI: CodeStar is an advanced coding assistant powered by StarCoder 2 """

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


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


# Syntax Highlighting
def print_highlighted(code: str) -> None:
    """
    Highlight and print the provided code.

    Args:
        code (str): The code to be highlighted and printed.
    """

    console = Console()
    md = Markdown(code, code_theme="github-dark", justify="left")

    console.print(
        Panel(
            md,
            title_align="left",
            title="[bold green]CodeStar[/bold green]",
        )
    )
