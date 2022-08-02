"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cofog."""


if __name__ == "__main__":
    main(prog_name="cofog")  # pragma: no cover
