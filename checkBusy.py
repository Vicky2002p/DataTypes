# checkBusy.py
# A program to count the number of people entering an area and output if it is busy or not.
# Area could be any place like gym, restaurant, hotel, etc 

import tkinter as tk
from tkinter import simpledialog
counter = 0     # to keep a count of entered names

window = tk.Tk()
window.withdraw()         # to hide the additional box that appears

space = 10      # defines the available gym equipiments or tables at restaurant or rooms at hotel 
list = []       # for making a list of people

for num in range(0, space):
    name = simpledialog.askstring(title = "checkBusy", prompt = "Please put in your name: ")
    if name is None or name.strip() == "":
        break
    else:
        list.append(name)
        counter += 1

# conditions for comparing
if counter <= space*0.30:
    print("It is mostly empty.")
# num of people less than 30% of space available
if counter <= space*0.50 and counter > space*0.30:
    print("Half of it is empty.")
# num of people in the range 30% to 50% space available
if counter <= space*0.80 and counter > space*0.50:
    print("The store is busier then usual.")
# num of people greater than or equal to 80% of space available
if space*0.80 <= counter:
    print("It is very busy.")

window.destroy()  # close the window and end the program