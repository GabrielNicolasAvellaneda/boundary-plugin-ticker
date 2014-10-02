#/usr/bin/env python
import ystockquote
import sys
import string

"""
Implements a plugin that gets current stock price and volume
"""

# We need to have two arguments the second being the ticker symbol
if len(sys.argv) == 2:
  # Make uppercase
  ticker = sys.argv[1].upper()
  price = ystockquote.get_price(ticker)
  volume = ystockquote.get_volume(ticker)
  if volume != 'N/A':
    print('{0} {1} {2}'.format('BOUNDARY_STOCK_PRICE',price,ticker))
    print('{0} {1} {2}'.format('BOUNDARY_STOCK_VOLUME',volume,ticker))
