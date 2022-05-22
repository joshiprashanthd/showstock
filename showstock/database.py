import configparser
import json
from pathlib import Path
from typing import Dict, NamedTuple, Optional, Any

from showstock import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_showstock.json")


def get_database_path(config_file: Path) -> Path:
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:
    try:
        db_path.write_text("\{\}")  # Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR


class DBResponse(NamedTuple):
    data: Optional[Dict[str, Any]]
    status: int


class DatabaseHandler:
    def __init__(self, db_path: Path):
        self._db_path = db_path

    def read(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.decoder.JSONDecodeError:
                    return DBResponse(None, JSON_ERROR)
        except OSError:
            return DBResponse(None, DB_READ_ERROR)

    def write(self, data: Dict[str, Any]) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(data, db, indent=4)
            return DBResponse(data, SUCCESS)
        except OSError:
            return DBResponse(data, DB_WRITE_ERROR)
