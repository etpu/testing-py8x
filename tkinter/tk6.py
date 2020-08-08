""" Библиотека Tkinter - 6 - События мыши
https://www.youtube.com/watch?v=TSyT1uOCZms&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=6 """

from tkinter import *


def left_click(ecent):
    frame_1.configure(bg="red")
    frame_2.configure(bg="white")
    frame_3.configure(bg="white")


def middle_click(ecent):
    frame_1.configure(bg="white")
    frame_2.configure(bg="red")
    frame_3.configure(bg="white")


def right_click(ecent):
    frame_1.configure(bg="white")
    frame_2.configure(bg="white")
    frame_3.configure(bg="red")


tk = Tk()

tk.configure(bg="black")

frame_1 = Frame(tk, width=250, height=250, bg="white")
frame_2 = Frame(tk, width=250, height=250, bg="white")
frame_3 = Frame(tk, width=250, height=250, bg="white")

frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1, padx=1)
frame_3.grid(row=0, column=2)

tk.bind("<Button-1>", left_click)
tk.bind("<Button-2>", middle_click)
tk.bind("<Button-3>", right_click)

tk.mainloop()
