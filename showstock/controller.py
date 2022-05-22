from pathlib import Path
from typing import NamedTuple, Optional, Dict, Any

import typer
from showstock import SUCCESS
from showstock import database
from showstock.database import DatabaseHandler
from showstock import config


class CTResponse(NamedTuple):
    data: Optional[Dict[str, Any]]
    status: int


class AppController:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)

    def add_symbol(self, symbol: str, category: str = "general") -> CTResponse:
        """
        Add a [symbol] to the database with the given [category].
        """
        symbol = symbol.upper().strip()
        category = category.strip()

        read_response = self._db_handler.read()
        if read_response.status != SUCCESS:
            return CTResponse(None, read_response.status)

        read_response.data.setdefault(category, []).append(symbol)

        write_response = self._db_handler.write(read_response.data)
        if write_response.status != SUCCESS:
            return CTResponse(None, write_response.status)

        return CTResponse({category: write_response.data[category]}, SUCCESS)


def get_controller():
    if config.CONFIG_DB_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_DB_PATH)
    else:
        typer.secho(
            "Config file not found. Please run 'showstock init'", fg=typer.colors.RED
        )
        raise typer.Exit(1)

    if db_path.exists():
        return AppController(db_path)
    else:
        typer.secho(
            "Database file not found. Please run 'showstock init'", fg=typer.colors.RED
        )
        raise typer.Exit(1)
