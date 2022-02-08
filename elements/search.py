from tkinter import *
from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()

# user clicks into search_field
#   event listener on click clears default text
def clear_search_default(event):
    """[clear the default text of the Entry widget and set cursor to index: 0 ]

    Args:
        event (<Double-Button-1>): [tk.event pattern double click left mouse button]
    """   
    curr_txt = event.widget.get()
    event.widget.delete(0, END)
    event.widget.icursor(0)
    
def search_keyword(keyword):
    url = 'https://www.alphavantage.co/query?'
    query = {
       
        'keywords' : keyword.get(),
        'function': 'SYMBOL_SEARCH',
        'apikey' : os.environ.get('API_KEY')
    }

    req = requests.get(url, params=query)
    print(req.content)
    keyword.delete(0, END)
# user clicks search button
#   create query object with value of search field and url
#   query search endpoint of alphavantage api
#   render results as a frame of label widgets with main query callback




# Query API with user selection from the search results to request the relevant data from the applicable AlphaVantage API endpoints
# add results as records to DB Tables
# render categorical results to the appropriate readout_frame as label widgets with charting callbacks

# !!! In order for the keyword_select_result callback to make alterations to the readout frames, import the readout widgets and pass them as the default values of set parameters so that when the function is set as a callback in main.py, no additional arguments need to be passed. 