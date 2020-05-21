import pandas as pd
import copy
import yfinance as yf
from wallstreet import Call, Put, Stock

def find_closest_strike(strikes, stock_price):
  start= 0
  end= len(strikes)-1
  
  while(start<=end):
    mid= (start+end)//2
    if (stock_price == strikes[mid]): 
      return strikes[mid]
    if ((end-start) == 1):
      if (abs(stock_price - strikes[start]) < abs(stock_price - strikes[end])):
        return strikes[start]
      else: 
        return strikes[end]
    if (end == start):
      return strikes[end]
    if (stock_price < strikes[mid]):
      end= mid
    else:
      start= mid

def get_stock_iv(option, stock_price):
  option = copy.copy(option)
  strikes = list(option.strikes)
  strike = find_closest_strike(strikes, stock_price)
  option.set_strike(strike)
  return option.implied_volatility() * 100, strike

def get_option(ticker, d=12, m=2, y=2016, option_type=Call):
  try:
    return option_type(ticker, d=d, m=m, y=y)
  except:
    raise

def get_stats(holdings, limit=100):
  stock_list = []
  exceptions = []
  for ticker in holdings[:limit]:
    try:
      option = get_option(ticker)
      stock = option.underlying
      iv, strike = get_stock_iv(option, stock.price)
      msft = yf.Ticker('MSFT')
      marketCap = msft.info['marketCap']
      stock_list.append((ticker, marketCap, iv, strike))
    except Exception as e:
      exceptions.append((ticker, str(e)))
  return stock_list, exceptions