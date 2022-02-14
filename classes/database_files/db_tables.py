'''File contains Class Definitions for the various Database tables used to store data from API Calls.
'''
# Imports:
import psycopg2
import datetime as dt 


class CompanyTicker:
    """Class defines values of table columns for database unless positional arguments are passed on instantiation. table stores general identifying data from company search results and will be referenced by other tables in the database.
    """
    def __init__(
        self, 
        name:str, 
        symbol:str, 
        region:str, 
        type_:str, 
        currency:str
        ):

        self.name = name or 'VARCHAR(120)'
        self.symbol = symbol or 'VARCHAR(20)'
        self.region = region or 'VARCHAR(60)'
        self.type_ = type_ or 'VARCHAR(20)'
        self.currency = currency or 'VARCHAR(10)'
        self.date_added =  str(dt.date.today().strftime("%x")) if self.name != 'VARCHAR(120)' else 'DATE NOT NULL'
        

    def __str__(self):
        return f'Instance of a Company Searched for, includes name, symbol, currency and date it was added to the database.'
        

    def __repr__(self):
        return f'{str(self.__class__(self.name, self.symbol, self.region, self.type_, self.currency))} \n {self.__dict__} \n '
       

    
    