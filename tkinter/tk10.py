"""Библиотека Tkinter - 10 - Выпадающее меню
https://www.youtube.com/watch?v=rRE-GgE8ajE&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=10 """

from tkinter import *

def new_win():
    win = Toplevel(tk)
    label_1 = Label(win, text="Текст в окне верхнего уровня", font=20)
    label_1.pack()

def exit_app():
    tk.destroy()



tk = Tk()

main_menu = Menu(tk)
tk.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="File", menu=first_item)
first_item.add_command(label="New", command=new_win)
first_item.add_command(label="Exit", command=exit_app)

second_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=second_item)
second_item.add_command(label="Item1")
second_item.add_command(label="Item2")
second_item.add_command(label="Item3")
second_item.add_separator()
second_item.add_command(label="Item4")

tk.mainloop()