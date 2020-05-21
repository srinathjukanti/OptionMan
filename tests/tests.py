import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from option_man import get_holdings_csv

def test_get_holdings_csv():
    csv = get_holdings_csv("sp500-constituents.csv")
    assert csv.is_file()==True

