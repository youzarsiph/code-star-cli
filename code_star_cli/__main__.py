""" Allows to run the CLI using python -m """

from code_star_cli.main import code_star


def main() -> None:
    """Entry point function for running the CLI."""

    # Run the cli
    code_star(prog_name="code-star")


if __name__ == "__main__":
    main()
