#/usr/bin/env python
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import ystockquote
import sys
import string
import time
import json

class Ticker():
	"""Implements a meter plugin that gets current stock price and volume"""
	def __init__(self, pollInterval):
		self.pollInterval = pollInterval

	def loadParameters(self):
		""" Reads the meter plugin runtime parameters"""
		json_data = open("param.json")
		data = json.load(json_data)
		self.items = data["items"]

	def sendEvent(self):
		pass

	def sendMeasurement(self,metric,value,source,timestamp):
		""" Sends measurements to standard out to be read by plugin manager"""
		sys.stdout.write('{0} {1} {2} {3}\n'.format(metric,value,source,timestamp).decode('utf-8'))
		sys.stdout.flush()

	def run(self):
		"""Plugin main loop"""
		self.loadParameters()
		self.sendEvent()
		while True:
			# Loop over the items and lookup the stock price and volume
			for i in self.items:
				ticker = str(i["ticker"]).upper()
    			price = ystockquote.get_price(ticker)
    			volume = ystockquote.get_volume(ticker)
    			if volume == 'N/A' or price == 'N/A':
    				self.sendEvent()
    				sys.exit(1)
    			else:
    				timestamp = int(time.time())
    				self.sendMeasurement('BOUNDARY_STOCK_PRICE',price,ticker,timestamp)
    				self.sendMeasurement('BOUNDARY_STOCK_VOLUME',volume,ticker,timestamp)
				time.sleep(self.pollInterval)

if __name__ == "__main__":
    plugin = Ticker(10)
    plugin.run()





