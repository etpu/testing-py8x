"""Библиотека Tkinter - 17 - Анимированная отрисовка
https://www.youtube.com/watch?v=vLFnh3iCp_8&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=17 """

from tkinter import *
from math import sin, cos

x=0

def print_dot():
    global x

    y1 = sin(x)
    y2 = cos(x)

    cvs.create_oval(25 * x + 10, 25 * y1 + 100, 25 * x + 10, 25 * y1 + 100, width=1, outline="red")
    cvs.create_oval(25 * x + 10, 25 * y2 + 100, 25 * x + 10, 25 * y2 + 100, width=1, outline="blue")

    x += 0.03

    tk.after(5, print_dot)

tk = Tk()

cvs = Canvas(tk, width=600, height=200, bg="white")
cvs.pack()

cvs.create_line(10, 0, 10, 200, width=2, arrow="both", fill="grey")
cvs.create_line(10, 100, 600, 100, width=2, arrow="last", fill="grey")

print_dot()


tk.mainloop()