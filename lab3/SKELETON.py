from tkinter import *
import tkinter as tk
import random
from tkinter import ttk
from tkinter import Menu
import random


win = tk.Tk()
win.title("GUI Python")
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()

positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(win.winfo_screenheight() / 2 - windowHeight / 2)

win.geometry("500x300+{}+{}".format(positionRight, positionDown))

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


menu_bar = Menu(win)
win.config(menu=menu_bar)


class Lights:
    red_light = None
    yellow_light = None
    green_light = None
    red = None
    yellow = None 
    green = None


class Led():
    def __init__(self, canvas, tab):
        self.canvas = canvas
        self.tab = tab
        self.draw_led()

    def activate(self):
        color = IntVar()
        Lights.red = Radiobutton(self.tab, text="red", value=1, variable=color, command=lambda:check_red(self))
        Lights.yellow = Radiobutton(self.tab, text="yellow", value=2, variable=color, command=lambda:check_yellow(self))
        Lights.green = Radiobutton(self.tab, text="green", value=3, variable=color, command=lambda:check_green(self))
        
        Lights.red.grid(row=0, column=1)
        Lights.yellow.grid(row=0, column=2)
        Lights.green.grid(row=0, column=3)

    def deactivate(self):
        self.paint('#ccc')
        Lights.red.configure(state = DISABLED)
        Lights.yellow.configure(state = DISABLED)
        Lights.green.configure(state = DISABLED)

    def paint(self, color='white'):
        self.canvas.itemconfig(Lights.red_light, fill=color)
        self.canvas.itemconfig(Lights.yellow_light, fill=color)
        self.canvas.itemconfig(Lights.green_light, fill=color)

    def draw_led(self):
        Lights.red_light = self.canvas.create_oval(20,20,80,80, width = 1, fill = "white")
        Lights.yellow_light = self.canvas.create_oval(20,80,80,140, width = 1, fill = "white")
        Lights.green_light = self.canvas.create_oval(20,140,80,200, width = 1, fill = "white")


def tipa_laba2(chk, led):  
    led.paint()
    if(chk.get()):
        led.activate()
    else:
        led.deactivate()
        

def check_red(led):
    led.paint()
    led.canvas.itemconfig(Lights.red_light, fill='red')


def check_yellow(led):
    led.paint()
    led.canvas.itemconfig(Lights.yellow_light, fill='yellow')


def check_green(led):
    led.paint()
    led.canvas.itemconfig(Lights.green_light, fill='green')
        

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

def laba2():
    tabControl = ttk.Notebook(win)  # Create Tab Control

    sheet1 = tk.Frame(tabControl)

    tab1 = tk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='Завдання 1')  # Add the tab
    canvas = tk.Canvas(tab1, width=200, height=200)
    canvas.grid()

    traffic = ttk.LabelFrame(tab1, text=' Світлофор ')
    traffic.grid(column=0, row=0, padx=8, pady=4)

    remove_control = ttk.LabelFrame(tab1, text=' Пульт ')
    remove_control.grid(column=0, row=1, padx=8, pady=4)

    led = Led(canvas, tab1)
    led.activate()
    led.deactivate()
    write_lighter = IntVar()
    python_checkbutton = Checkbutton(remove_control, text="Увімкнути", variable=write_lighter,
        onvalue=1, offvalue=0, command=lambda:tipa_laba2(write_lighter, led))
    python_checkbutton.grid()


    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    '''python_lang = IntVar()
    python_checkbutton = Checkbutton(tab1, text="Python", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10, command=lambda:tipa_laba2(python_lang))
    python_checkbutton.grid(row=0, column=0, sticky=W)
'''

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Лаба 1", command=laba1)
file_menu.add_command(label="Лаба 2", command=laba2)
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