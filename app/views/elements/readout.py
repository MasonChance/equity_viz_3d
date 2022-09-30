'''Contains Class defining the readout section of the main application window where detailed information regarding the company stock is made available. 
'''
import tkinter as tk
from dotenv import load_dotenv
import requests
import json
import os
import sys
load_dotenv()

from ...schemas_templates.rdout_schema import RDOUT_SCHEMA

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
        self.rdout_frame = tk.Frame(self.master)
        self.rdout_frame.config(
            width=568,
            height=500,
            borderwidth=2,
            highlightcolor='#cac6f2',
            highlightbackground='#575760',
            relief='sunken'
            
        )

        # self.rdout_lines = self.li_items()
        self.rdout_frame.grid_propagate(0)
        self.render_li_items()
     
    def render_li_items(self):
        # iterates RDOUT_SCHEMA and adds a Line_Item instance to the Readout.rdout_frame for each key in RDOUT_SCHEMA
        for idx, data_set in enumerate(RDOUT_SCHEMA):
            Line_Item(data_set, idx, self.rdout_frame)
        
        

        


    # TODO: define a callback for the "get" button in the rdout_item
    # callback should open a dialog box that allows selection of parameters for the query and on "show" constructs and executes the API Query. rendering the results in a new application window.


class Line_Item:
    def __init__(self, li_item:object, row:int, master=None):
        # line item is comprised of: a frame containing a label and a button
        self.master = master
        self.item_frame = tk.Frame(self.master)
        
        self.row = row
        # self.item_frame.grid_propagate(0)
        self.item_frame.grid(row=row, column=0, pady=5)
        

        self.li_item = li_item
        # Instantiate the Label widget to display the "gui_name" property of the 
        item = tk.Label(self.item_frame)
        item.config(
            width=20,
            fg='#000000',
            text=li_item['gui_name'],
            anchor= tk.W 
        )
        
        item.grid_propagate(0)
        item.grid(row=0, column=0,pady=2)

        # TODO: set up button Decide if button should bring up a sort of "query configuration" window and if so how should it gain access to the necessary information for the query. 
