#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro

GUI in Python 3
Using Tkinter
"""

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
import os

Path = r"path to app form C://"

# Create instance
window = tk.Tk()

# Title of the window    
window.title("Media Organization GUI")

# Label to media
ttk.Label(window, text="Which media would you like to access?").grid(column=0, row=0)

# Button Click Event Function
def click_me():
    action.configure(os.startfile(Path, "open"))

# Button
action = ttk.Button(window, text="Go!", command=click_me)   
action.grid(column=1, row=1)

#======================
# Start GUI
#======================
window.mainloop()