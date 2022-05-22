import json
from pathlib import Path
from typing import Optional

import pytest
from showstock import SUCCESS, controller


@pytest.fixture()
def mock_json_file(tmp_path: Path) -> Path:
    data = {"general": ["TSLA", "AMZN", "BTC-USD"]}
    db_path = tmp_path / "mock_db.json"
    with db_path.open("w") as db:
        json.dump(data, db, indent=4)
    return db_path


test_data1 = {
    "args": {"symbol": "GOOG", "category": "general   "},
    "return": {
        "data": {
            "general": ["TSLA", "AMZN", "BTC-USD", "GOOG"],
        },
    },
}

test_data2 = {
    "args": {"symbol": "BTC-USD", "category": "crypto"},
    "return": {
        "data": {
            "crypto": ["BTC-USD"],
        },
    },
}


@pytest.mark.parametrize(
    "symbol, category, expected",
    [
        (
            test_data1["args"]["symbol"],
            test_data1["args"]["category"],
            test_data1["return"]["data"],
        ),
        (
            test_data2["args"]["symbol"],
            test_data2["args"]["category"],
            test_data2["return"]["data"],
        ),
    ],
)
def test_add_symbol(
    mock_json_file: Path, symbol: str, category: Optional[str], expected: dict
):
    app_controller = controller.AppController(mock_json_file)
    response = app_controller.add_symbol(symbol, category)
    assert response.status == SUCCESS
    assert response.data == expected
