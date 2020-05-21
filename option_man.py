import pandas as pd
import yfinance as yf
import json
from option_helpers import get_stats
from pathlib import Path

def get_holdings_csv(name="sp500-constituents.csv"):
    holdings_dir = Path("holdings/")
    sp500_holdings = holdings_dir / name

def tickers():
    holdings_csv = get_holdings_csv()
    holdings_df = pd.read_csv(holdings_csv)
    tickers = list(holdings_df['Symbol'])
    return tickers

def calcStockStats(tickers):
    stocks, exceptions = get_stats(tickers, limit=len(tickers))
    return stocks, exceptions

def filterHighMarketCap(stocks, limit=100):
    stocks.sort(key=lambda x:x[1], reverse=True) 
    return stocks[:limit]

stocks = calcStockStats(tickers())
stocks = filterHighMarketCap(stocks)
stocks.sort(key=lambda x:x[2], reverse=True)

stocks_json = json.dumps(dict(stocks))
print(stocks_json)

# stocks, exceptions = get_holdings_iv(holdings=sp500_tickers, limit=10)
# highIvFirst=True
# stocks.sort(key=lambda x:x[0], reverse=highIvFirst)

# print('High IV Stocks\n', stocks)
# print('Run Time Exceptions\n', exceptions)