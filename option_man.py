from option_helpers import get_holdings_iv
import pandas as pd

holdings_dir = './holdings'
holdings_df = pd.read_csv(holdings_dir.'/sp500-constituents')
sp500_tickers = list(holdings_df['Symbols'])
stocks, exceptions = get_holdings_iv(holdings=sp500_tickers, limit=10)
highIvFirst=True
stocks.sort(key=lambda x:x[0], reverse=highIvFirst)

print('High IV Stocks\n', stocks)
print('Run Time Exceptions\n', exceptions)