#/usr/bin/env python
import ystockquote
import sys
import string
import time
import json

"""
Implements a plugin that gets current stock price and volume
"""

if len(sys.argv) == 1:
  pollInterval = 20

json_data = open("param.json")
data = json.load(json_data)
# Loop over the items and lookup the stock price and volume
items = data["items"]
while True:
  for i in items:
    ticker = str(i["ticker"]).upper()
    price = ystockquote.get_price(ticker)
    volume = ystockquote.get_volume(ticker)
    if volume != 'N/A':
      print('{0} {1} {2}'.format('BOUNDARY_STOCK_PRICE',price,ticker))
      print('{0} {1} {2}'.format('BOUNDARY_STOCK_VOLUME',volume,ticker))
  time.sleep(pollInterval)
