""" CodeStar CLI: CodeStar is an advanced coding assistant powered by StarCoder 2 """

from typing import Optional
from rich.markdown import Markdown
from rich.panel import Panel


# Constants
CHAT_LLM = "HuggingFaceH4/starchat2-15b-v0.1"
COMPLETION_LLM = "bigcode/starcoder2-15b"
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are CodeStar, an advanced coding assistant powered by StarCoder 2, "
    "a state-of-the-art Large Language Model for Code trained on over 600 programming "
    "languages from a diverse set of permissively licensed data, including GitHub code, "
    "Arxiv, and Wikipedia. CodeStar is specifically optimized for enhanced performance in "
    "coding tasks. You also a senior software engineer, software architect, site reliability "
    "engineer and cybersecurity expert.",
}


def create_panel(title: str, content: str, subtitle: Optional[str] = None) -> Panel:
    """
    Highlight and print the provided code.

    Args:
        title (str): Panel title.
        content (str): Panel content.
        subtitle (str, optional): An optional subtitle for the panel.

    Returns:
        Panel
    """

    md = Markdown(content, code_theme="lightbulb")

    return Panel(
        md,
        title=f"[bold green]{title}[/bold green]",
        title_align="left",
        subtitle=subtitle,
        subtitle_align="right",
    )
