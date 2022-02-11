'''File contains Class Definitions for the various Database tables used to store data from API Calls.
'''
# Imports:
import psycopg2
import datetime as dt 


class CompanyTicker:
    """[ DB.table recording name, ticker symbol as symbol, region, currency, type and foregin key. NOTE: type must be referenced as type_ to avoid keyword conflict]
    """
    def __init__(self, name:str, symbol:str, region:str, type_:str, currency:str) -> object:
        self.name = name
        self.symbol = symbol
        self.region = region
        self.type_ = type_
        self.currency = currency
        self.date_added = str(dt.date.today().strftime('%x'))
        

    def __str__(self):
        return f'Instance of a Company Searched for, includes name, symbol, currency and date it was added to the database.'
        

    def __repr__(self):
        return f'{str(self.__class__(self.name, self.symbol, self.region, self.type_, self.currency))} \n {self.__dict__} \n '
       

    
    