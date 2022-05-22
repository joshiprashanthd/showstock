"""
CLI
"""

from pathlib import Path
from subprocess import call
from typing import Optional

import typer

from showstock import (
    ERRORS,
    SUCCESS,
    __appname__,
    __version__,
    __author__,
    database,
    config,
)
from showstock.app import App

app = typer.Typer()


@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        help="Set the database path",
        prompt="Database Path",
    )
) -> None:
    """
    Initialize the database
    """
    init_app_status = config.init_app(db_path)

    if init_app_status != SUCCESS:
        typer.secho(
            f"Creating config file failed with {ERRORS[init_app_status]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    init_database_status = database.init_database(Path(db_path))

    if init_database_status != SUCCESS:
        typer.secho(
            f"Creating database failed with {ERRORS[init_database_status]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"Database Path is {db_path}", fg=typer.colors.GREEN)


def _version_callback(value: bool) -> None:
    if value:
        typer.secho(f"{__appname__} v{__version__}", fg=typer.colors.BRIGHT_CYAN)
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=_version_callback,
    ),
) -> None:
    """
    Starts displaying stock quotes.
    """
    if ctx.invoked_subcommand is None:
        gui = App()
        gui.run()
