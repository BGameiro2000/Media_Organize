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

# Start file function
def run(Path):
    os.startfile(Path, "open")

# Create instance
win = tk.Tk()   

# Add a title
win.title("Media")

# First, we define the app paths and the apps name
Apps = ["Name displayed", "Música", "Fotos"]
Paths = ["Path to the app", "C:\\Program Files (x86)\\MAGIX\\MP3 deluxe 19\\MP3deluxe.exe", "F:\\VLC\\vlc.exe"]
AppsPath = dict(zip(Apps, Paths))

# Radiobutton Callback
def radCall():
    radSelect=radNumberVar.get()
    if radSelect == 1:
        App = AppsPath[Apps[1]]
    elif radSelect == 2:
        App = AppsPath[Apps[2]

# create two Radiobuttons using one variable
radNumberVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
while variable  in range(Apps):
    for i in range(Apps):
        i += 1
        radNumberVar.set(i)
 
# Now we are creating all three Radiobutton widgets within one loop
for ap in range(1, Apps):
    curRad = tk.Radiobutton(win, text=Apps[ap], variable=radNumberVar, value=ap, command=radCall)
    curRad.grid(column=ap, row=2, sticky=tk.W)

# Button Click Event Function
def click_me():
    action.configure(run(App))

# Adding a Button
action = ttk.Button(win, text="Go!", command=click_me)
action.grid(column=1, row=1)
action.configure(state='disabled')

#======================
# Start GUI
#======================
win.mainloop()