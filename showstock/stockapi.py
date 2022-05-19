import requests
from showstock.stockdata import StockData

def get_stock_data(symbol: str) -> StockData:
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + symbol
    response = requests.get(url, headers={
        'User-Agent': ''
    })
    data = response.json()
    data =  data['quoteResponse']['result'][0] 
    return StockData(
        marketState=data['marketState'],
        price=data['regularMarketPrice'],
        symbol=data['symbol'],
        marketChange=data['regularMarketChange'],
        marketChangePercent=data['regularMarketChangePercent'],
        currency=data['currency']
    )
