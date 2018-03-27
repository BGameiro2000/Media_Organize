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

#======================
# title
#======================
# Title of the window    
window.title("Media Organization GUI")

#======================
# label
#======================
# Label to media
ttk.Label(window, text="Which media would you like to access?").grid(row=0)

#======================
# go button
#======================
# Button Click Event Function
def click_me():
    action.configure(os.startfile(Path, "open"))

# Button
action = ttk.Button(window, text="Go!", command=click_me)
action.grid(column=4, row=1, sticky=tk.E)

#======================
# radio buttons
#======================
# Radiobutton global variables (list)
Apps = ["Name displayed", "Música", "Fotos"]
Paths = ["Path to the app", "C:\\Program Files (x86)\\MAGIX\\MP3 deluxe 19\\MP3deluxe.exe", "F:\\VLC\\vlc.exe"] #-r
rPaths = []
AppsPath = dict(zip(Apps, rPaths))

# Radiobutton Callback
def radioCall():
    radioSelect=radioVariable.get()
    if   radioSelect == 0: radioSelect = 0 #nothing appens
    elif radioSelect == 1: window.configure("""add path to app 1""")
    elif radioSelect == 2: window.configure("""add path to app 2""")
    else: window.configure("""add path to app 2""")
# create three Radiobuttons using one variable
radioVariable = tk.IntVar()

# Selecting a non-existing index value for radioVariable
radioVariable.set(0)

# Creating all Radiobutton widgets within one loop
for ap in range(1, len(Apps)):
    curRad = tk.Radiobutton(window, text=Apps[ap], variable=radioVariable, value=ap, command=radioCall)
    curRad.grid(column=ap, row=1, sticky=tk.E)

#======================
# Start GUI
#======================
window.mainloop()