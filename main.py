from tkinter import *
from elements.search import clear_search_default, search_keyword

# Define and Configure main application window
main_win = Tk()
main_win.title('Equity 3D')
main_win.geometry('600x700')


# Navbar and Search frame: configs and position
nav_frame = Frame(main_win)
nav_frame.configure(
    width=590,
    height=50
    
)


nav_frame.grid_propagate(0)
nav_frame.grid(row=0, column=0, padx=5, pady=5)


# <Search Field> Entry; placement and config

search_field = Entry(nav_frame)
search_field.configure(
    font=('Comic Sans', 12, 'italic'), 
    fg='#dbdbdb',

)
search_default='Enter Ticker or Company to search'
search_field.insert(ANCHOR, search_default)
search_field.grid(row=0, column=0, padx=5, pady=10)
search_field.bind('<Double-Button-1>', clear_search_default, add='+')
# <Search Button>: placement, config. handler && callback imported from app.py
search_btn = Button(nav_frame, width=10, text='Search', command=lambda: search_keyword(search_field))
search_btn.grid(row=0, column=1, padx=5, pady=15, sticky=E)

# <Clear Button>: placement, config. handler && callback imported from app.py
clear_btn = Button(nav_frame, width=10, text='Clear')
clear_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)

# <Config 3D Button>: placement, config. handler && callback imported from app.py
# This should open a seperate window for selecting which elements to add to the 3D model and defining its axes.
config_3d_btn = Button(nav_frame, width=10, text='Config 3D')
config_3d_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

# Info and Tooltip Frame: placement, config, default values
info_frame = Frame(main_win, width=570, height=100)
info_frame.configure(
    borderwidth=2, 
    relief=SUNKEN, 
    highlightthickness=2,
    highlightcolor='#cac6f2', 
    highlightbackground='#575760'
)

info_frame.grid_propagate(0)
info_frame.grid(row=1, column=0, pady=5)

info_text = Text(info_frame, width=570, height=5)
# TODO: create a "tooltip:Default" message and insert the variable here instead of hard coding. this should be done at the time of developing the tooltip utility. 
info_text.insert(END, "Tooltips and Information will be displayed here")

info_text.configure(
    font=('Comic Sans', 12), 
    state='disabled'
)

info_text.grid(row=0, column=0)

# Results from search Frame
results_frame = Frame(main_win)
results_frame.configure(
    width=570,
    height=480
)
results_frame.grid_propagate(0)
results_frame.grid(row=2, column=0, padx=2.5, pady=10)


# <Fundamental Data Readout>: Frame placement, config; contents of this frame will be altered/updated dynamically as a result of using the application. see Callback for <search_btn>
fundamnt_readout = Frame(results_frame)
fundamnt_readout.configure(
    width=280,
    height=480,
    background='#9f99f7',
    borderwidth=1, 
    relief=SUNKEN, 
    highlightthickness=1,
    highlightcolor='#cac6f2', 
    highlightbackground='#575760'
)

fundamnt_readout.grid_propagate(0)
fundamnt_readout.grid(row=1, column=0, padx=2.5, pady=10, sticky=W)

# <Technical Data Readout>: Frame placement, config; contents of this frame will be altered/updated dynamically as a result of using the application. see Callback for <search_btn>

technic_readout = Frame(results_frame)
technic_readout.configure(
    width=280,
    height=480,
    background='#9f99f7',
    borderwidth=1, 
    relief=SUNKEN, 
    highlightthickness=1,
    highlightcolor='#cac6f2', 
    highlightbackground='#575760'
)

technic_readout.grid_propagate(0)
technic_readout.grid(row=1, column=1, padx=5, pady=15, sticky=W)



main_win.mainloop()