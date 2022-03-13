'''Contains Class defining the base application window.
'''
import tkinter as tk 
from .elements.nav import Nav 


class Home:

    def __init__(self, master=None):
        nav = Nav(master)
        nav.nav_frame.grid(row=0, column=0, padx=5, pady=5)
        # call info class instance
        # call readout class instance
        


