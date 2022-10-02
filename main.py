"""Main application loop runs here. Install, first-time setup, and main application loop should run here.
"""
import sys
import os 
import tkinter as tk 
from app.UI.display_windows.home import Home

main_win = tk.Tk()
main_win.title('3D Viz')
main_win.geometry('600x700')

def main(home, main_win):
    home(main_win)
    main_win.mainloop()



if __name__ == "__main__":
    
    main(Home, main_win)