#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro
Dictionary to use in Media Organization Menu project
GUI in Python 3
Using Tkinter
"""

#======================
# imports
#======================
import re
from Data.UserSettings.userlists import Apps as Apps
from Data.UserSettings.userlists import Paths as Paths

#======================
# create rPaths to escape the backslash
#======================
BSDouble = r"\\"
BSDoubleDouble = r"\\\\"
rPaths = [re.sub(BSDouble, BSDoubleDouble, p) for p in Paths]

#======================
# create AppsPath dictionary
#======================
AppsPath = dict(zip(Apps, rPaths))