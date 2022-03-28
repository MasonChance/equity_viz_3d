'''This File Defines a schema/configuration dict for the Readout Class itemizing the information to be displayed and the parameters required for a call to the API.
'''


rdout = {
    "overview" : {
        "gui_name" : "Overview",
        
        "req_params" : {
            "function" : "OVERVIEW",
        },

        "opt_params" : None,
    },

    "income" : {
        "gui_name" : "Income Statement",
        
        "req_params" : {
            "function" : "INCOME_STATEMENT",
        },

        "opt_params" : None,
    },

    "balance" : {
        "gui_name" : "Balance Sheet",

        "req_params" : {
            "function" : "BALANCE_SHEET",
        },

        "opt_params" : None,
    },

    "cash" : {
        "gui_name" : "Cash Flow Statement",

        "req_params" : {
            "function" : "CASH_FLOW",
        },

        "opt_params" : None,
    },

    "earnings" : {
        "gui_name" : "Earnings Statements",

        "req_params" : "EARNINGS",

        "opt_params" : None,
    },

    

}
    