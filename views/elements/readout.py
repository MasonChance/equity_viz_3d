'''Contains Class defining the readout section of the main application window where detailed information regarding the company stock is made available. 
'''
import tkinter as tk
from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()

from app.rdout_schema import RDOUT_SCHEMA as rc 
# Each Line Item of the Readout should contain the folowing items
#   Information title, eg: SMA, Income Statement, STOCH, RSI etc
#   Time Series Interval, (if applicable) eg: 1min, daily, monthly etc
#   Time Series Period, (if applicable) eg: last month, last year etc
#   Series Type, (if applicable) eg: open, close, high, low etc
#   Other Indicators regarding the shape/scope of the data available

# Each Line Item should Contain actionable buttons/clickables allowing the user to:
#   View a Chart of the data, (Chart should be a new window)
#   retrieve the data with custom time_series_interval, series_period, and series_type. 
#   Save the Data to local for use in the 3dConfig

class Readout:
    def __init__(self, master=None):
        self.master = master
        self.rdout = tk.Frame(self.master)
        self.rdout.config(
            width=590,
           
        )

        self.rdout.grid_propagate(0)
        

       
        for idx, item in enumerate(rc):
            # call a function that creates a listbox item and adds it to the listbox, passing the item as an argument
            self.rdout_item(rc[f"{item}"], idx)





    def rdout_item(self, item, idx):
       
        # Create a frame widget to be added as a listbox item
        item_frame = tk.Frame(self.rdout)
        item_frame.config(
            width=300,
            height=300,
            padx=5,
            pady=10,
        )
        item_frame.grid(row=idx, column=0)
        # Create a text widget to identify the item (eg: Balance sheet)
        item_label = tk.Label(item_frame)
        
        item_txt = item["gui_name"]
        item_label.config(
            width=280,
            text=item_txt,
        )
        item_label.grid(row=idx, column=0, sticky='W')
        # Create a button widget to "get" the info callback should bring up an option dialog box that allows a choice of "show as chart" or "show as table" as well as allowing the selection of any optional or additional parameters allowed by the api
        item_btn = tk.Button(item_frame)
        item_btn.configure(
            width=80,
            text='Get'
        )
        item_btn.grid(row=idx, column=1, sticky='E')
        


    # TODO: define a callback for the "get" button in the rdout_item
    # callback should open a dialog box that allows selection of parameters for the query and on "show" constructs and executes the API Query. rendering the results in a new application window.