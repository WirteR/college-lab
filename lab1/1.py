import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.geometry("200x100")

ttk.Label(win, text="Моя перша програма").grid(column=0, row=0)

win.mainloop()