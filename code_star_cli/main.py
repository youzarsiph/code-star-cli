""" CodeStar CLI """

import typer
from code_star_cli.commands import command_list


code_star = typer.Typer(
    name="code-star",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="CodeStar CLI, an advanced AI-powered coding assistant.",
)


# Add the commands
for command in command_list:
    code_star.command(no_args_is_help=True)(command)


if __name__ == "__main__":
    code_star()
