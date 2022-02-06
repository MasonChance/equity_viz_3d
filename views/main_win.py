from tkinter import *


# Define and Configure main application window
main_win = Tk()
main_win.title('Equity 3D')
main_win.geometry('700x600')

# Search Field Label and Entry; placement and config
search_field = Entry(main_win, width=30)
search_field.grid(row=0, column=0,padx=10, pady=15)

# MVP setup will require user to delete the default text manually. future updates will add an event listener to automatically select the whole field and highlight it so that the default text is replaced when the user begins typing in the field

search_field.insert(0, "Enter Ticker or Company to Search")
search_field.configure(font=('Comic Sans', 12, 'italic'), fg='#dbdbdb')

# Search Button: placement, config, and handler/callback
search_btn = Button(main_win, width=10, text='Search')
search_btn.grid(row=0, column=1, padx=5, pady=15)

# Clear Button: placement, config, and handler/callback
clear_btn = Button(main_win, width=10, text='Clear')
clear_btn.grid(row=0, column=2, padx=5, pady=15)

# Config 3D Button: placement, config and handler/callback
# This should open a seperate window for selecting which elements to add to the 3D model and defining its axes.
config_3d_btn = Button(main_win, width=10, text='Config 3D')
config_3d_btn.grid(row=0, column=3, padx=5, pady=15)

# Info and Tooltip Frame: placement, config, default values
info_frame = Frame(main_win, width=700, height=200)
info_frame.grid(row=1, columnspan=4, padx=5, pady=10)

info_text = Text(info_frame, width=45, height=5, padx=5, bg='#dbdbdb', relief=SUNKEN)
# TODO: create a "tooltip:Default" message and insert the variable here instead of hard coding. this should be done at the time of developing the tooltip utility. 
info_text.insert(END, "Tooltips and Information will be displayed here")
info_text.configure(font=('Comic Sans', 16, 'bold'), state='disabled')
info_text.grid(row=0, column=0, columnspan=4)



main_win.mainloop()