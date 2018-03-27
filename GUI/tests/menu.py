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

# Create instance
window = tk.Tk()

# Title of the window    
window.title("Media Organization GUI")

# Label to media
ttk.Label(window, text="Which media would you like to access?").grid(column=0, row=0)

#======================
# Start GUI
#======================
window.mainloop()