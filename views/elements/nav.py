import tkinter as tk

class Nav():
    def __init__(self, master=None):
        self.nav_frame = tk.Frame(master)
        self.nav_frame.config(
            width = 590,
            height = 50,
        )
        self.nav_frame.propagate(0)
        self.search_field()
        self.search_btn()


    def search_field(self):
        search_field = Entry(self.nav_frame)
        search_field.insert(0, "Enter Ticker or Company to Search")

        search_field.configure(
            font=('Comic Sans', 12, 'italic'), 
            fg='#dbdbdb'
        )

        search_field.grid(row=0, column=0, padx=5, pady=10)
        

    def search_btn(self):
        search_btn = Button(nav_frame, width=10, text='Search')
        # FIXME: button still needs callback command=lambda: search_keyword(self.nav_frame)
        search_btn.grid(row=0, column=1, padx=5, pady=15, sticky=E)