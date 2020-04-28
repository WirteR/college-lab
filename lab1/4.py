from tkinter import ttk
import tkinter as tk

win = tk.Tk()

def change():
    win.title(e.get())

lbl = ttk.Label(win, text="Введіть новий заголовок").grid(row=0)

e = tk.Entry(win)
e.grid(row=1)

button1 = ttk.Button(win, command=change, text="Змінити заголовок").grid(column=0, row=2)

win.geometry("200x100")

win.mainloop()