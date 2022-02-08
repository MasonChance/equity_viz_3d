from tkinter import *
import requests
import json


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
    
    
# user clicks search button
#   create query object with value of search field and url
#   query search endpoint of alphavantage api
#   render results as a frame of label widgets with main query callback




# Query API with user selection from the search results to request the relevant data from the applicable AlphaVantage API endpoints
# add results as records to DB Tables
# render categorical results to the appropriate readout_frame as label widgets with charting callbacks

