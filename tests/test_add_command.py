from typer.testing import CliRunner

from showstock import cli


def test_add_with_category() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.app, ["add", "BTC-USD"], input="another\n")
    assert result.exit_code == 0
    assert 'Added symbol "BTC-USD" to category "another"' in result.output


def test_add_with_explicit_option() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.app, ["add", "ETH-USD", "--category", "crypto"])
    assert result.exit_code == 0
    assert 'Added symbol "ETH-USD" to category "crypto"' in result.output


def test_add_without_category() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.app, ["add", "RELIANCE-USD"], input="\n")
    assert result.exit_code == 0
    assert 'Added symbol "RELIANCE-USD" to category "general"' in result.output
