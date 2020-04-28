from tkinter import ttk
import tkinter as tk

win = tk.Tk()

def post():
    ttk.Label(win, text="Привіт").grid(column=0, row=0)

def close_window():
    win.destroy()

button1 = ttk.Button(win, command=post, text="Привіт").grid(column=0, row=1)
buttom2 = ttk.Button(win, command=close_window, text="Exit").grid(column=1, row=1)

win.geometry("200x100")

win.mainloop()