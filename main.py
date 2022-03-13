"""Main application loop runs here. Install, first-time setup, and main application loop should run here.
"""
import tkinter as tk 
from views.home import Home

main_win = tk.Tk()
main_win.title('3D Viz')
main_win.geometry('600x700')





if __name__ == "__main__":
    Home = Home(main_win)
    main_win.mainloop()