"""Библиотека Tkinter - 16 - Работа с Canvas (статические изменения фигур)
https://www.youtube.com/watch?v=mZOOB2cBMZg&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=16 """

from tkinter import *


def create_outline(event):
    c1.itemconfigure(oval1, outline="blue", width=3)


def change_fill(event):
    c1.itemconfigure(oval2, fill="orange")
    c1.coords(oval2, 250, 10, 390, 90)


def move_ovals(event):
    c1.move("ovals", 0, 260)


def clear_canvas(event):
    c1.delete("all")

tk = Tk()

c1 = Canvas(tk, width=400, height=400, bg="white")
c1.pack()

oval1 = c1.create_oval(10, 10, 90, 90, width=0, fill="red", tag="ovals")
oval2 = c1.create_oval(310, 10, 390, 90, width=0, fill="blue", tag="ovals")
triangle = c1.create_polygon(200, 200, 10, 390, 390, 390, fill="green")

c1.tag_bind(oval1, "<Button-1>", create_outline)
c1.tag_bind(oval2, "<Button-1>", change_fill)
c1.tag_bind(triangle, "<Button-1>", move_ovals)
tk.bind("<Button-3>", clear_canvas)

tk.mainloop()
