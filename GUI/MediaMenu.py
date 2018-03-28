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
from tkinter import ttk, Menu
from tkinter import messagebox as msg
import os
from Data.dictionary import AppsPath as AppsPath
from Data.UserSettings.userlists import Apps as Apps

# Create instance
window = tk.Tk()

#======================
# functions
#======================
def runApp():
    radioSelect = radioVariable.get()
    action.configure(state="normal")
    global thisApp
    thisApp = AppsPath[Apps[radioSelect]]

# Button Click Event Function
def click_me():
    os.startfile(thisApp, "open")

# Exit GUI cleanly
def quit():
    window.quit()
    window.destroy()
    exit()

#======================
# title
#======================
# Title of the window    
window.title("Media Organizer GUI")

#======================
# label
#======================
# Label to media
ttk.Label(window, text="Which media would you like to access?").grid(row=0)

#======================
# radio buttons
#======================
# create three Radiobuttons using one variable
radioVariable = tk.IntVar()

# Selecting a non-existing index value for radioVariable
radioVariable.set(0)

# Creating all Radiobutton widgets within one loop
for ap in range(1, len(Apps)):
    curRad = tk.Radiobutton(window, text=Apps[ap], variable=radioVariable, value=ap, command=runApp)
    curRad.grid(column=ap, row=1, sticky=tk.E)

#======================
# go button
#======================
# Button
action = ttk.Button(window, text="Go!", command=click_me)
action.grid(column=4, row=1, sticky=tk.E)
action.configure(state="disabled")

#======================
# menu bar
#======================
# Creating a Menu Bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Add menu items
# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Help")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)

#======================
# Start GUI
#======================
window.mainloop()