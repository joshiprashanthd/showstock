"""
CLI
"""

from typing import Optional

import typer

from showstock import __appname__, __version__, __author__
from .app import App

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__appname__} v{__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    gui = App()
    gui.run()
