""" Библиотека Tkinter - 5 - Метод bind
https://www.youtube.com/watch?v=kLY0O_me8-s&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=5 """

from tkinter import *

def output(event: int):

    try:
        txt = int(entry_1.get())
        if txt < 18:
            label_1["text"] = "Вам ещё рано сюда!"
        elif txt >= 18:
            label_1["text"] = "Добро пожаловать!"
        else:
            label_1["text"] = "Ошибка!"
    except ValueError:
        label_1["text"] = "Введите корректный возраст!"

tk = Tk()
tk.title("Сколько вам лет?")

entry_1 = Entry(tk, width=3, font=15)
button_1 = Button(tk, text="Проверить")
label_1 = Label(tk, width=27, font=15)

entry_1.grid(row=0, column=0)
button_1.grid(row=0, column=1)
label_1.grid(row=0, column=2)

button_1.bind("<Button-1>", output)

tk.mainloop()