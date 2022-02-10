'''Defines functions for making api calls to the various endpoints required by the application. All Querry URLs begin with 'https://www.alphavantage.co/query?'. differentiate endpoints by desginating the correct value for the <function> API parameter.
'''

# Imports
from tkinter import *
from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()

# Global Variables:
url = os.environ.get('API_URL')


# API Call Function Definitions

class Query:
    def __init__(self, keywords, function):
        self.symbol = symbol
        self.function = function
        self.apikey = os.environ.get('API_KEY')
        self.datatype = 'json'

# Fundamental Data Endpoints:
        
    # TODO: get Income Statement Endpoint: function=INCOME_STATEMENT

    # TODO: get Balance Sheet Endpoint: function=BALANCE_SHEET

    # TODO: get Cash Flow statement: function=CASH_FLOW

    # TODO: get Earnings Data: function=EARNINGS

    # TODO: get Overview : function=OVERVIEW



# Technical Indicators Endpoints: 

    # TODO: get SMA (simple moving average) function=SMA. Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get WMA. (weighted moving average) function=WMA Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get STOCH (stochastic oscillator values) function=STOCH Endpoint requires additional parameters to be set: interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; optional params : fastkperiod=int(default=5), slowkperiod=int(default=3), slowdperiod=int(default=3), slowkmatype=range(0, 8). see alphavantage docs for other matypes avalable as options

    # TODO: get RSI (relative strength index) function=RSI: Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get ADX (average directional movement index) function=ADX: Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get ROC (rate of change) function=ROC : Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get MFI (money flow index) function=MFI: Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get DX (directional movement index) function=DX: Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); series_type=[close, open, high, low]

    # TODO: get MIDPRICE (highets + lowest)/2 function=MIDPRICE: Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated); 

    # TODO: get TRANGE (true range) function=TRANGE : Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; 
    
    # TODO: get ATR (average true range) function=ATR : Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly]; time_period=int(total datapoints to be calculated);

    # TODO: get OBV (on balance volume) function=OBV : Endpoint requires additional parameters to be specified with predetermined values. interval=[1min, 5min, 15min, 30min, 60min, daily, weekly, monthly];

    