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
        event (<Button-1>): [tk.event pattern click left mouse button in search_field]
    """   
    curr_txt = event.widget.get()
    event.widget.delete(0, END)
    event.widget.icursor(0)


def result_selected(event):
    print(event.widget.get(ANCHOR))
    # 


def search_keyword(nav_frame):
    # user clicks search button
    # create query object with value of search field and url
    url = 'https://www.alphavantage.co/query?'
    query = {
       
        'keywords' : nav_frame.winfo_children()[0].get(),
        'function': 'SYMBOL_SEARCH',
        'apikey' : os.environ.get('API_KEY')
    }

    # query search endpoint of alphavantage api and delete the contents of the search_field
    req = requests.get(url, params=query).json()

    nav_frame.winfo_children()[0].delete(0, END)
    # print(req)
    nav_frame.config(
        height=150
    )
    # render results as a Listbox widget inside a Frame
    # Create, configure, and position the result Frame
    result_frame = Frame(nav_frame)
    result_frame.configure(
        width=nav_frame.winfo_reqwidth(),
        height=150,
    )
    result_frame.grid_propagate(0)
    result_frame.grid(row=1, column=0, columnspan=4, padx=5,sticky=NW)

    # Create, configure, populate, and positon the result Listbox
    result_list = Listbox(result_frame)
    result_list.configure(
        font=('Comic Sans', 12),
        width=result_frame.winfo_reqwidth(),
        
        # height=40,
    )

    # FIXME: add scrollbox for the result_frame/list

    for result in req['bestMatches']:

        result_fstr = f' {result["1. symbol"]}, {result["2. name"], result["4. region"]} '
        result_list.insert(END, result_fstr)

    result_list.grid(row=0, column=0, columnspan=4,sticky=NW)
    result_list.bind('<<ListboxSelect>>', result_selected)



# Query API with user selection from the search results to request the relevant data from the applicable AlphaVantage API endpoints
# add results as records to DB Tables
# render categorical results to the appropriate readout_frame as label widgets with charting callbacks

# !!! In order for the keyword_select_result callback to make alterations to the readout frames, import the readout widgets and pass them as the default values of set parameters so that when the function is set as a callback in main.py, no additional arguments need to be passed. 