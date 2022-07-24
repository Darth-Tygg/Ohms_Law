# This is Program calculates Ohm's Law. Written by Ryan Adams. 7-23-2022
'''
IR = V
V/R = I
V/I = R

VI = W

V**2 / R = W
I**2 * R = W
'''

import pyinputplus as py
import tkinter as tk
from tkinter import *

# Creating a GUI Window
window = Tk()
window.title("Ohm's Law")


# Create Buttons
def voltage_button_click():
    i = int(ei.get())
    r = int(er.get())
    v = i * r
    e_answer.insert(0, v)


def current_button_click():
    v = int(ev.get())
    r = int(er.get())
    i = v / r
    e_answer.insert(0, i)


def resistance_button_click():
    v = int(ev.get())
    i = int(ei.get())
    r = v / i
    e_answer.insert(0, r)


def power_button_click():
    v = int(ev.get())
    i = int(ei.get())
    r = int(er.get())
    w = v * i
    w = v**2 / r
    w = i**2 * r
    e_answer.insert(0, w)


def clear_button_click():
    ev.delete(0, END)
    ei.delete(0, END)
    er.delete(0, END)
    e_answer.delete(0, END)


# Create Entry boxes
ev = Entry(window, width=20, borderwidth=5, bg='black', fg='aqua')
ev.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

ei = Entry(window, width=20, borderwidth=5, bg='black', fg='aqua')
ei.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

er = Entry(window, width=20, borderwidth=5, bg='black', fg='aqua')
er.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

e_answer = Entry(window, width=20, borderwidth=5, bg='black', fg='aqua')
e_answer.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


# Define Buttons
button_1 = Button(window, text="Volts", padx=26, pady=20, command=lambda: voltage_button_click())
button_2 = Button(window, text="Amps", padx=26, pady=20, command=lambda: current_button_click())
button_3 = Button(window, text="Ohms", padx=26, pady=20, command=lambda: resistance_button_click())
button_4 = Button(window, text="Watts", padx=26, pady=20, command=lambda: power_button_click())
button_5 = Button(window, text="Clear", padx=26, pady=20, command=lambda: clear_button_click())

# Put Buttons on screen
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=0)
button_3.grid(row=2, column=0)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)

# This tells Python to run the Tkinter event loop.
window.mainloop()
