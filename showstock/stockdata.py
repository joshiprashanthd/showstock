class StockData:
    def __init__(self, marketState, price, symbol, marketChange, marketChangePercent, currency):
        self.marketState = marketState
        self.price = price
        self.symbol = symbol
        self.marketChange = marketChange
        self.marketChangePercent = marketChangePercent
        self.marketState = marketState
        self.currency = currency

    def __str__(self):
        return f"({self.symbol}): {self.price}"
    
    def __repr__(self) -> str:
        return f"({self.symbol}): {self.price}"

    def __eq__(self, other) -> bool:
        return self.price == other.price