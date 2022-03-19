import tkinter as tk 

class Info:

    def __init__(self, master=None):
        self.master = master
        self.contents = "Tooltips and Information will be displayed here"

        self.info_frame = tk.Frame(self.master)
        self.info_frame.configure(
            width=570,
            height=100,
            borderwidth=2,
            highlightcolor='#cac6f2',
            highlightbackground='#575760',
        )

        self.info_frame.grid_propagate(0)
        self.text_contents()
        
    
    def text_contents(self):
        text = tk.Text(self.info_frame)
        #!!! must insert default text or alter text prior to configureing state as DISABLED. to alter the text of the info field you must re-assign the value of self.contents and then invoke the text_contents method.  
        text.insert(tk.END, self.contents)

        text.configure(
            width=570,
            height=10,
            font=('Comic Sans', 12),
            fg='#000000',
            state=tk.DISABLED,
            
        )

        text.grid(row=0, column=0)

