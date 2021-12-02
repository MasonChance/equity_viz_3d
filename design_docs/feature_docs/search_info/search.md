# Search Field and Button

[Back to README](../../../README.md)
[Back to Design.md](../../design.md)

The following is an outline of the search field, its design attributes and interaction with the related button. Specifications will be separated between the field itself and the callable button.

**User Stories**
[General Use and GUI](../../user_stories/general_use_ui.md)

## Required Packages and Resources

For more details on a given resource, see [Packages And Libraries](../../pkg_lib.md).

*AlphaVantage API* the search feild should query the API for both company and ticker matches, and return a context box with the top 10 results. See [AlphaVantage Ticker Query](https://polygon.io/docs/get_v3_reference_tickers_anchor)

*Python Module: Request* built-in module for web request:response protocols.

*httpie: package* package for making http requests via terminal, used for testing the WRRC of this Application.

### Overview of Design Approach

In the effort to minimize extaneous API Calls the application should have a DB table that stores all active tickers and corresponding company names which can then be querried in place of the api for search function auto-suggest/results display; and only further query the API when a specific selection has been made. The DB table should be updated on application start only.

Future versions of the application may utilize an auto-suggest feature for the search field but for MVP search should only execute onClick of the search button and the top 10 results of the search should be displayed in a separate windowed frame that allows the user to click the desired result and have its data displayed in the main window, automatically closing the results frame on selection.

### List of Required Elements

- DB table of currently active Ticker:Company pairs
- Start-up function to update DB table from the API
- callback for search-button querries DB for ticker OR Company Name up to 4 matching Chars and opens a new window with top ten results
- results should have a callback that querries the API for further data and displays that data in the corresponding data lists in the main window (fundamental data, technical data).

### Description and Characteristics of Required elements

*Database Table:*
MVP will require only name and ticker pairs but in the interest of future proofing with optional search filters it should also include:

- market
- primary exchange
- type (common, preferred, etc)

*Start-up Script:*
This script should run on application start and query the API. For ease and speed the previous table should be dropped, a new table created based on a schema and populated as a result of the API query.

*Search-Button Callback:*
This callback should return all results that exactly match the search. If no matches are found it should return the results that match in descending order based on number of consecutive characters matching. In such a case results should be prioritized by length of the search term; if search term is less or equal to 4 chars, prioritize matching based on ticker, else based on company name.

*Result Callbacks:*
Each result displayed should have a callback that queries the api for the data defined in [Data Request](../data_request/data_req.md) and supplying its associated ticker to the API Request object.

**DB Table Diagram:**
![Ticker:Name Table]()

**Start-up Script WRRC:**
![Start-up Script]()

**Search-Button Algo/Whiteboard:**
![Search-Button Whiteboard]()

**Search Result Window Wireframe:**
![Search Result Wireframe]()
