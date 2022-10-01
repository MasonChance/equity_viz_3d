import tkinter as tk
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

from ..elements.nav import ALPHA_QUERY
from ...api_db_classes.query_cls import KeywordQuery, DetailQuery

# results configuration window should display the company and symbol the results are being obtained for (this is determined by the search term the user has previously selected in the main window)

# The additional paramaters (ie: time interval) should be displayed with option menues for selecting their chosen configuration

# this window also needs access to the rdout_schema object associated with the line item they have selected to configure the results for

# 