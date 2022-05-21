import configparser
from pathlib import Path

import typer

from showstock import DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __appname__

CONFIG_DIR_PATH = Path(typer.get_app_dir(__appname__))
CONFIG_DB_PATH = CONFIG_DIR_PATH / "config.ini"


def init_app(db_path: str) -> None:
    """
    Initialize the application by creating the config file and the database.

    :param db_path: Path to the database file.
    """

    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code

    db_code = _init_database(db_path)
    if db_code != SUCCESS:
        return db_code

    return SUCCESS


def _init_config_file() -> int:
    """
    Initialize the config file.

    :return: 0 if the config file was created successfully, otherwise non-zero value on failure.
    """
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except:
        return DIR_ERROR

    try:
        CONFIG_DB_PATH.touch(exist_ok=True)
    except:
        return FILE_ERROR

    return SUCCESS


def _init_database(db_path: str) -> None:
    """
    Initialize the database.

    :param db_path: Path to the database file.
    """
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}

    try:
        with CONFIG_DB_PATH.open("w") as file:
            config_parser.write(file)
    except:
        return DB_WRITE_ERROR

    return SUCCESS
