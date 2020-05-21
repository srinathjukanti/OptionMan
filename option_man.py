import pandas as pd
from option_helpers import get_holdings_iv
from pathlib import Path

def get_holdings_csv(name="sp500-constituents.csv"):
    holdings_dir = Path("holdings/")
    sp500_holdings = holdings_dir / name

# holdings_df = pd.read_csv(sp500_holdings)
# sp500_tickers = list(holdings_df['Symbol'])
# stocks, exceptions = get_holdings_iv(holdings=sp500_tickers, limit=10)
# highIvFirst=True
# stocks.sort(key=lambda x:x[0], reverse=highIvFirst)

# print('High IV Stocks\n', stocks)
# print('Run Time Exceptions\n', exceptions)