Boundary Stock Ticker Plugin
============================

Example Meter Plugin that provides the current stock price and volume of stock given its stock ticker.

### Prerequisites

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |


|  Runtime | node.js | Python | Java |
|:---------|:-------:|:------:|:----:|
| Required |         |   +    |      |


- [How to install Python?](https://help.boundary.com/hc/articles/202270132)
- Python [_ystockquote_](https://pypi.python.org/pypi/ystockquote) module


|Metric Name  |Metric Identifier      |Description                             |
|:------------|:----------------------|:---------------------------------------|
|Stock Price  |BOUNDARY\_STOCK\_PRICE |Current stock price for the current day |
|Stock Volume |BOUNDARY\_STOCK\_VOLUME|Current stock volume for the current day|

## Dashboards
Here are the list of dashboards that are created when the ticker plugin is installed with their descriptions.

|Dashboard|Description                                     |
|:--------|:-----------------------------------------------|
|Stocks   |Displays the current price and volume of a stock|
