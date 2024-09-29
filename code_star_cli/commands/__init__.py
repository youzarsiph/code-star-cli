""" CodeStar CLI commands """

from code_star_cli.commands.ai import ai
from code_star_cli.commands.chat import chat
from code_star_cli.commands.completions import completions
from code_star_cli.commands.enhance import enhance
from code_star_cli.commands.scan import scan


# Add your commands here
command_list = [ai, chat, completions, enhance, scan]
