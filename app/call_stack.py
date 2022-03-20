'''This Module defines a function responsible for making an API call for every endpoint indicated by the Fundamental and Technical query classes defined in api_db_classes/query_cls.py 
'''
from api_db_classes import AlphaVQuery, FundamentalQuery, TechnicalQuery

from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()

url = os.environ.get('API_URL')

def call_list(keyword:str)-> list:
    pass
    # TODO: loop for each key of FundamentalQuery
    # TODO: loop for each key of TechnicalQuery
    # at each iteration, response should be parsed into an SQL table. all other operations should be done from the table and not the response object. 
    