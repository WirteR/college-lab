from tkinter import *
import tkinter as tk
import random
from tkinter import ttk
from tkinter import Menu
import random
# Create instance
win = tk.Tk()
# Add a title
win.title("GUI Python")
# Gets the requested values of the height and widht.
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(win.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
win.geometry("500x300+{}+{}".format(positionRight, positionDown))

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


def b(tab3_label, num):
    tab3_label.config(text = "Вам випало {}".format(num))
    tab3_label.pack()


def b2(message):
    win.title(message.get())
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

        
def laba1():
    tabControl = ttk.Notebook(win)  # Create Tab Control

    sheet1 = tk.Frame(tabControl)

    tab1 = tk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='Завдання 1')  # Add the tab

    tab2 = tk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text='Завдання 2')  # Make second tab visible

    tab3 = tk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab3, text='Завдання 3')  # Make second tab visible

    tab4 = tk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab4, text='Завдання 4')  # Make second tab visible


    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    tab1_label = tk.Label(tab1, text = "Моя перша програма", fg="blue", font = ("Arial Bold", 20), bg = "yellow", width=300, height=2)
    tab1_label.pack()
    btn = Button(tab1, text="Click Me", padx="200", pady="2", font="12", command=_quit)
    btn.pack()


    tab2_label = tk.Label(tab2, text = "Hello, world", fg="blue", font = ("Arial Bold", 20), bg = "yellow", width=300, height=2)
    
    btn = Button(tab2, text="Click Me", font="12", command=lambda: tab2_label.pack(side = 'top'))
    btn.place(relx=.24, rely=.7, anchor="c", height=130, width=200, bordermode=OUTSIDE)
    #btn.pack(side = BOTTOM)

    btn = Button(tab2, text="Click Me", font="12", command=_quit)
    btn.place(relx=.74, rely=.7, anchor="c", height=130, width=200, bordermode=OUTSIDE)
    #btn.pack(side = BOTTOM)
    
    tab3_label = tk.Label(tab3, text = "Киньте кубик", fg="blue", font = ("Arial Bold", 20), bg = "yellow", width=300, height=2)
    btn = Button(tab3, text="Кинути кубик", font="12", command = lambda:b(tab3_label, random.randint(1,6)))
    btn.place(relx=.5, rely=.5, anchor="c", height=130, width=200, bordermode=OUTSIDE)

    tab4_label = tk.Label(tab4, text = "Введіть новий заголовок", fg="blue", font = ("Arial Bold", 20), bg = "yellow", width=300, height=2)
    tab4_label.pack()
    message = StringVar()
 
    message_entry = Entry(tab4, textvariable=message)
    message_entry.place(relx=.5, rely=.3, anchor="c")

    btn = Button(tab4, text="Змінити заголовок", font="12", command=lambda:b2(message))
    btn.place(relx=.5, rely=.7, anchor="c", height=130, width=200, bordermode=OUTSIDE)
    tab4_label.pack()


# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Лаба 1", command=laba1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="Tasks", menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)



#======================
# Start GUI
#======================
win.mainloop()