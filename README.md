boundary-plugin-ticker
======================

Plugin that provides the current stock price and volume of stock given its stock ticker.


The Boundary Plugins Development Guide uses the plugin to describe the tips and best practices for developing Boundary Premium metric plugins.


Prerequisites
-------------
The following items are required on the host platform in addition to the Boundary Premium [relay](http://premium-support.boundary.com/customer/portal/articles/1635550-plugins---how-to).
* Python 2.6.6 or later
* Python [_ystockquote_](https://pypi.python.org/pypi/ystockquote) module


|Metric Name |Description                             |
|------------|----------------------------------------|
|Stock Price |Current stock price for the current day |
|Stock Volume|Current stock volume for the current day|

## Dashboards
Here are the list of dashboards that are created when the ticker plugin is installed with their descriptions.

|Dashboard| Description                                    |
|---------|------------------------------------------------|
|Stocks   |Displays the current price and volume of a stock|
