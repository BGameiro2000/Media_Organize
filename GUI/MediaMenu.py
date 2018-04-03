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
from tkinter import simpledialog as dlg
import os
from Data.dictionary import AppsPath as AppsPath
from Data.UserSettings.userlists import Apps as Apps
import Data.Help.MediaMenuHelp as Help
import Data.Help.MediaMenuHowTo as HT

# Create instance
window = tk.Tk()

#======================
# functions
#======================
def _runApp():
    radioSelect = radioVariable.get()
    action.configure(state="normal")
    global thisApp
    thisApp = AppsPath[Apps[radioSelect]]

# Button Click Event Function
def _click_me():
    os.startfile(thisApp, "open")

# Help Message box
def _msgBoxHelp():
    msg.showinfo(Help.Title, Help.Message)

# How to Message box
def _msgBoxHT():
    msg.showinfo(HT.Title, HT.Message)

# Exit GUI cleanly
def _quit():
    window.quit()
    window.destroy()
    exit()

# Add app to the GUI
def _addApp():
    addApp = dlg.SimpleDialog(window, title="Add Apps")

# Remove app from the GUI
def _removeApp():
    removeApp = dlg.SimpleDialog(window, title="Remove Apps")

#======================
# title
#======================
# Title of the window    
window.title("Media Organizer GUI")

#======================
# label
#======================
# Label to media
ttk.Label(window, text="Which media would you like to access?").grid(column=0, row=0)

#======================
# container
#======================
# Create container
button_frame = ttk.LabelFrame(window, text="Apps available:")
button_frame.grid(column=0, row=1)

#======================
# radio buttons
#======================
# create three Radiobuttons using one variable
radioVariable = tk.IntVar()

# Selecting a non-existing index value for radioVariable
radioVariable.set(0)

# Creating all Radiobutton widgets within one loop
for ap in range(1, len(Apps)):
    curRad = tk.Radiobutton(button_frame, text=Apps[ap], variable=radioVariable, value=ap, command=_runApp)
    curRad.grid(column=ap, row=1, sticky=tk.E)

#======================
# go button
#======================
# Button
action = ttk.Button(window, text="Go!", command=_click_me)
action.grid(column=0, row=2)
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
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Add apps", command=_addApp)
edit_menu.add_separator()
edit_menu.add_command(label="Remove apps", command=_removeApp)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="How to...", command=_msgBoxHT)
help_menu.add_separator()
help_menu.add_command(label="Help", command=_msgBoxHelp)
menu_bar.add_cascade(label="Help", menu=help_menu)

#======================
# menu bar
#======================


#======================
# Start GUI
#======================
window.mainloop()  