from typer.testing import CliRunner

from showstock import cli
from showstock import __version__, __appname__


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{__appname__} v{__version__}\n"
