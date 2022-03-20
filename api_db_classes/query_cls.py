'''Class definition for query object to be used with the AlphaVantage API
'''
from dotenv import load_dotenv
import json
import os
load_dotenv()

alpha_vantage_url = os.environ.get('API_URL')

class AlphaVQuery:
    def __init__(self, keywords, function):
        self.url = alpha_vantage_url
        self.keywords = str(keywords )
        self.function = str(function)
        self.apikey = os.environ.get('API_KEY')
        self.datatype = 'json'

    def __str__(self):
        return f'query object used in request to AlphaVantage API'

    def __repr__(self):
        return f'{self.keys()}'


class FundamentalQuery:
    def __init__(self):
        self.income = 'INCOME_STATEMENT'
        self.balance = 'BALANCE_SHEET'
        self.cash = 'CASH_FLOW'
        self.earnings = 'EARNINGS'
        self.overview = 'OVERVIEW'

    def __str__(self):
        return f'class defining the api endpoints required for company fundamental data'

    def __repr__(self):
        return f'{self.keys()}'

    

class TechnicalQuery:
    def __init__(self):
        pass
    # TODO: these queries differ as they require additional parameters 