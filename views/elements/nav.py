'''Contains Class defining the navigation frame widget, its components and related callbacks/event bindings
'''
import tkinter as tk
# from dotenv import load_dotenv
# import requests
# import json
# import os
# load_dotenv()

class Nav:
    def __init__(self, master=None):
        self.master = master 
        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.config(
            width = 590,
            height = 50,
        )
        self.nav_frame.propagate(0)
        self.search_field()
        self.search_btn()
        self.clear_btn()
        self._3d_conf()


    def search_field(self):
        search_field = tk.Entry(self.nav_frame)
        search_field.insert(0, "Enter Ticker or Company to Search")

        search_field.configure(
            font=('Comic Sans', 12, 'italic'), 
            fg='#dbdbdb'
        )

        search_field.grid(row=0, column=0, padx=5, pady=10)
        search_field.bind('<Button-1>', self.clear_search_default, add='+')


    
    def clear_search_default(self, e):
        """[clear the default text of the Entry widget and set cursor to index: 0 ]
        Args:
            event (<Button-1>): [tk.event pattern click left mouse button in search_field]
        """   
        curr_txt = e.widget.get()
        e.widget.delete(0, tk.END)
        e.widget.icursor(0)



    def search_btn(self):
        search_btn = tk.Button(self.nav_frame)
        search_btn.configure(
            width=10,
            text='Search',
        )

        #TODO: button still needs callback command=lambda: search_keyword(<search_widget>) because the command requires creation of a new frame and listbox anchored to the search field widget, create a subclass of Nav called: SearchMatches. use an instance of this class to get and display the possible matches. 

        search_btn.grid(row=0, column=1, padx=5, pady=15, sticky="E")


    def clear_btn(self):
        clear_btn = tk.Button(self.nav_frame)
        clear_btn.configure(
            width=10,
            text='clear',
        )

        #TODO: requires a command function to clear results

        clear_btn.grid(row=0, column=2, padx=5, pady=15, sticky="E")


    def _3d_conf(self):
        _3d_conf = tk.Button(self.nav_frame)
        _3d_conf.configure(
            width=10,
            text='3D Config',
        )

        #TODO: requires command functon to select and set the options and axis of the 3d rendered chart

        _3d_conf.grid(row=0, column=3, padx=5, pady=15, sticky="E")



# class SearchMatches(Nav):

#     def __init__(self, master=None):
#         self.master = master
#         self.match_frame = tk.Frame(self.master)

