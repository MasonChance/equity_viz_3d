'''Contains Class defining the readout section of the main application window where detailed information regarding the company stock is made available. 
'''
import tkinter as tk
from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()

from app.rdout_schema import RDOUT_SCHEMA 
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
            width=568,
            height=500,
            borderwidth=2,
            highlightcolor='#cac6f2',
            highlightbackground='#575760',
            relief='sunken'
            
        )

        self.rdout.grid_propagate(0)
        self.rdout_item(RDOUT_SCHEMA)
     
    
        

    def rdout_item(self, schema):
        
        for idx, item in enumerate(schema):
        
            # Create a text widget to identify the item (eg: Balance sheet)
            item_label = tk.Text(self.rdout)
            
            item_txt = schema[item]['gui_name']
            item_label.config(
                width=300,
                height=50,
                fg='#000000',
                font=('Comic Sans', 12),
                state=tk.DISABLED,
            )

            item_label.insert(tk.END, item_txt)
           
            item_label.grid(row=idx, column=0, sticky='W')
            # # Create a button widget to "get" the info callback should bring up an option dialog box that allows a choice of "show as chart" or "show as table" as well as allowing the selection of any optional or additional parameters allowed by the api
            # item_btn = tk.Button(self.rdout)
            # item_btn.configure(
            #     width=80,
            #     text='Get',
            #     font=('Comic Sans', 12),
            #     command=None,
            # )

            # item_btn.grid_propagate(0)
            # item_btn.grid(row=idx, column=1, sticky='E')
            continue
        


    # TODO: define a callback for the "get" button in the rdout_item
    # callback should open a dialog box that allows selection of parameters for the query and on "show" constructs and executes the API Query. rendering the results in a new application window.