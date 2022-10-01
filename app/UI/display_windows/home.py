'''Contains Class defining the base application window, and instantiating its child elements
'''
import tkinter as tk 
from .elements.nav import Nav 
from .elements.info import Info
from .elements.readout import Readout

class Home:

    def __init__(self, master=None):
        self.master = master

        # call nav class instance
        nav = Nav(self.master)
        nav.nav_frame.grid(row=0, column=0, padx=5, pady=5)
        
        # call info class instance
        info = Info(self.master)
        info.info_frame.grid(row=1, column=0, pady=5)
        
        # call readout class instance
        rdout = Readout(self.master)
        rdout.rdout_frame.grid(row=2, column=0,pady=5)
        # rdout.rdout_item()
        

    
