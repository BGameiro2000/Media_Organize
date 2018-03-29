#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro
Program to change the apps and their paths in order to use menu.py
GUI in Python 3
Using Tkinter
"""

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk, Menu
from tkinter import messagebox as msg
import Data.Help.ChangeAppHelp as Help
import Data.Help.ChangeAppHowTo as HT

# Create instance
window = tk.Tk()

#======================
# functions
#======================
# Exit GUI cleanly
def quit():
    window.quit()
    window.destroy()
    exit()

# Help Message box
def msgBoxHelp():
    msg.showinfo(Help.Title, Help.Message)

# How to Message box
def msgBoxHT():
    msg.showinfo(HT.Title, HT.Message)

#======================
# title
#======================
# Add a title
window.title("App changer")

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
file_menu.add_command(label="Exit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="How to...", command=msgBoxHT)
help_menu.add_separator()
help_menu.add_command(label="Help", command=msgBoxHelp)
menu_bar.add_cascade(label="Help", menu=help_menu)

#======================
# Start GUI
#======================
window.mainloop()