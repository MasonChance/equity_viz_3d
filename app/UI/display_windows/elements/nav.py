'''Contains Class defining the navigation frame widget, its components and related callbacks/event bindings
'''
import tkinter as tk
from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()

from ....api_dir.query_cls import KeywordQuery



# Global Variable to be used as Base Query object for GET-requests to the API. use the methods '_update_keyword' and '_update_function' to set the appropriate parameters for each sucessive API call.
ALPHA_QUERY = KeywordQuery()

class Nav:
    """Class defining the main navigation of the application window, including bindings
    and callbacks for the buttons. All child widgets of the Nav instance, are rendered
    and positioned via methods defined in the class and called in the __init__ function.
    """
    
    def __init__(self, master=None):
        self.master = master 
        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.config(
            width = 590,
            height = 50,
        )
        # self.nav_frame.propagate(0)
        self.search_field()
        self.search_btn()
        self.clear_btn()
        self._3d_conf_btn()


# ============ Search Field and related widgets and Callbacks ==========
    def search_field(self):
        """Defines the Search Field as a Tkinter Entry widget, its configuration, positioning, and bindings. 
        """
        search_field = tk.Entry(self.nav_frame)
        search_field.insert(0, "Enter Ticker or Company to Search")

        search_field.configure(
            font=('Comic Sans', 12, 'italic'), 
            fg='#dbdbdb'
        )

        search_field.grid(row=0, column=0, padx=5, pady=10)
        search_field.bind('<Button-1>', self.clear_search_default, add='+')
        

    
    def clear_search_default(self, e):
        """[A Callback function bound to the Search Field. Clears the default text of the Entry widget and sets cursor to index: 0 ]
        Args:
            event (<Button-1>): [tk.event pattern click left mouse button in search_field]
        """   
        curr_txt = e.widget.get()
        e.widget.delete(0, tk.END)
        e.widget.config(fg='black')
        e.widget.icursor(0)



    def search_btn(self):
        """Defines the Search Button as a Tkinter Button widget, its configuration, positioning, and bindings 
        """
        search_btn = tk.Button(self.nav_frame)
        search_btn.configure(
            width=10,
            text='Search',
            command=self.search_keyword
        )

        search_btn.grid(row=0, column=1, padx=5, pady=15, sticky="E")

    
    def search_keyword(self):
        """A Callback function bound to the Search Button. Gets the Search Field contents and uses it to get possible matches from the AlphaVantage API. Invokes a function to create a match result display and renders the results to the user.
        """
        # define necessary variables for the api query including the query object
        search_key = self.nav_frame.winfo_children()[0].get()
        ALPHA_QUERY._update_keyword(search_key)
        ALPHA_QUERY._update_function('SYMBOL_SEARCH')
        
        # assign the request to a variable
        req = requests.get(ALPHA_QUERY.url, params=ALPHA_QUERY.params).json()
        
        # delete the search feild input
        self.nav_frame.winfo_children()[0].delete(0, tk.END)

        # call match_display
        self.match_display()
        # assign variable to the listbox to avoid excessive bracket access. 
        matches = self.nav_frame.winfo_children()[-1].winfo_children()[0]
        # loop through request and insert fstring in listbox for each element. 
        
        for match in req["bestMatches"]:
            result_fstr = f'{match["1. symbol"]}, {match["2. name"]}'
            matches.insert(tk.END, result_fstr)

        
        matches.bind('<<ListboxSelect>>', self.selected_match)


    def match_display(self):
        """Defines a display for the Search Match results as a Tkinter Frame widget with a Tkinter Listbox; Defines configuration, and positioning.
        """
        #TODO: add scrollbar to the frame.
        match_frame = tk.Frame(self.nav_frame)
        match_frame.configure(
            width=self.nav_frame.winfo_reqwidth(),
            height=150,

        )
        match_frame.grid_propagate(0)
        match_frame.grid(row=1, column=0,columnspan=4, padx=5, pady=1)

        match_list = tk.Listbox(match_frame)
        match_list.configure(
            width=match_frame.winfo_reqwidth(),
            height=150,
            font=('Comic Sans', 12)
        )
        match_list.grid(row=0, column=0)


        

    def selected_match(self, e):
        # gets the selection and splits on "," assigns to the first element. This is based on the formatting contained in the 'search_keyword' method
        symbol = e.widget.get(e.widget.curselection()[0]).split(',')[0]
        # update the ALPHA_QUERY instance keyword with the symbol variable defined above
        ALPHA_QUERY._update_keyword(symbol)
        


    def clear_btn(self):
        clear_btn = tk.Button(self.nav_frame)
        clear_btn.configure(
            width=10,
            text='clear',
        )

        #TODO: requires a command function to clear results

        clear_btn.grid(row=0, column=2, padx=5, pady=15, sticky="E")


    def _3d_conf_btn(self):
        _3d_conf = tk.Button(self.nav_frame)
        _3d_conf.configure(
            width=10,
            text='3D Config',
        )

        #TODO: requires command functon to select and set the options and axis of the 3d rendered chart

        _3d_conf.grid(row=0, column=3, padx=5, pady=15, sticky="E")




   
