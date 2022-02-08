from tkinter import *
from main import search_field, fundamnt_readout, technic_readout
import requests
import json


# Get the value of the search_field 
#   Check that it is not default
#   Determine weather to use Ticker search or Company search
# Create Query Class Instance
#   pass in ticker || company parameter
#   pass in value of search_field
#   Querry class should create list of all applicable Querys
#
# loop through Querry instance making each successive Call
#   [] each call should be in a Try block. exception should return a custom exception object via a message box explaining which calls failed and what information is unavailable as a result
#   [] each result should be added to the appropriate table in the DB    
# Add result to DB
# Render results to page
