'''Class definition for query object to be used with the AlphaVantage API
'''
from dotenv import load_dotenv
import json
import os
load_dotenv()

alpha_vantage_url = os.environ.get('API_URL')

class KeywordQuery:
    def __init__(self, keyword=None, function=None):
        self.url = alpha_vantage_url
        self.params = {
            # !!! keywords attribute must be identified in the plural per the API documentation.
            "keywords" : keyword,
            "function" : function,
            "apikey" : os.environ.get('API_KEY'),
            "datatype" : 'json'
        }

    def __str__(self):
        return f'query object used in request to AlphaVantage API'

    def __repr__(self):
        return f'{self.keys()}'

    def _update_keyword(self, keyword):
        self.params['keywords'] = keyword

    def _update_function(self, function):
        self.params['function'] = function



class DetailQuery(KeywordQuery):
    def __init__(self, interval, time_period, series_type):
        super().__init__(self, keywords, function)
       
        self.params['interval'] = interval
        self.params['time_period'] = time_period
        self.params['series_type'] = series_type

    def __str__(self):
        return f'class defining the api call-parameters required for company serial data (ie: Simple Moving Average[SMA]) '

    def __repr__(self):
        return f'{self.keys()}'

    

