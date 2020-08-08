"""Библиотека Tkinter - 7 - События клавиатуры
https://www.youtube.com/watch?v=bh9zsbaLaGs&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=7 """

from tkinter import *

def print_char(event):
    label_1.configure(text=event.char)

def print_su(event):
    label_1.configure(text="Shift Up")

def print_cd(event):
    label_1.configure(text="Control Down")

tk = Tk()

label_1 = Label(tk, width=12, font=("Ubuntu", 100))
label_1.pack()

for i in range(65, 123):
    tk.bind(chr(i), print_char)

tk.bind("<Shift-Up>", print_su)
tk.bind("<Control-Down>", print_cd)


tk.mainloop()