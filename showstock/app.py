import time
from rich.table import Table
from rich.live import Live

from showstock.stockapi import get_stock_data


class App:
    def __init__(self, symbols=["AAPL", "MSFT", "GOOG"]):
        self.symbols = symbols
        self.data = None

    def updateData(self):
        self.data = {symbol: get_stock_data(symbol) for symbol in self.symbols}

    def genData(self):
        self.updateData()
        table = Table(title="Stock Prices", title_style="bold green")
        table.add_column("Symbol", justify="right")
        table.add_column("Price", justify="right")
        table.add_column("Change", justify="right")
        table.add_column("% Change", justify="right")
        table.add_column("Market State", justify="right")

        for symbol in self.symbols:
            curr = self.data[symbol]
            table.add_row(
                curr.symbol,
                str(curr.price),
                f"{'[red blink]' if curr.marketChange < 0 else '[green blink]'}"
                + str(curr.marketChange),
                f"{'[red blink]' if curr.marketChangePercent < 0 else '[green blink]'}"
                + str(curr.marketChangePercent),
                f"{'[red]' if curr.marketState == 'CLOSED' else '[green]'}{curr.marketState}",
            )

        return table

    def run(self):
        with Live(self.genData(), transient=True) as live:
            while True:
                time.sleep(1)
                live.update(self.genData())
