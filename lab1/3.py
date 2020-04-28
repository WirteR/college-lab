from tkinter import ttk
import tkinter as tk
import random

win = tk.Tk()

def throw():
    ls = [1, 2, 3, 4, 5, 6]
    ch = str(random.choice(ls))
    ttk.Label(win, text="вам випало "+ch).grid(column=0, row=0)

button1 = ttk.Button(win, command=throw, text="Кинути кубик").grid(column=0, row=1)

win.geometry("200x100")

win.mainloop()