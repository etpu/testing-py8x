"""Библиотека Tkinter - 11 - Панель инструментов и статус бар
https://www.youtube.com/watch?v=KZEYWURHBPo&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=11 """

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

toolbar = Frame(tk, bg="#A1A1A1")
toolbar.pack(side=TOP, fill=X)

btn1 = Button(toolbar, text="Cut")
btn1.grid(row=0, column=0, padx=2, pady=2)

btn2 = Button(toolbar, text="Copy")
btn2.grid(row=0, column=1, padx=2, pady=2)

btn3 = Button(toolbar, text="Paste")
btn3.grid(row=0, column=2, padx=2, pady=2)

statusbar = Label(tk, relief=SUNKEN, anchor=W, text="Mission complete.")
statusbar.pack(side=BOTTOM, fill=X)

tk.mainloop()