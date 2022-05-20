import requests
from showstock.stock import Stock
import typer


def get_stock_data(symbol: str) -> Stock:
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + symbol
    try:
        response = requests.get(url, headers={"User-Agent": ""})
    except:
        typer.secho("Cannot connect to the Internet!", fg=typer.colors.RED)
        raise typer.Exit(1)
    data = response.json()
    data = data["quoteResponse"]["result"][0]
    return Stock(
        marketState=data["marketState"],
        price=data["regularMarketPrice"],
        symbol=data["symbol"],
        marketChange=data["regularMarketChange"],
        marketChangePercent=data["regularMarketChangePercent"],
        currency=data["currency"],
    )
