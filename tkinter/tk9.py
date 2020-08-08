""" Библиотека Tkinter - 9 - Использование ООП
https://www.youtube.com/watch?v=GhkyLQ6A6Yw&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=9 """

from tkinter import *

class Question:
    """Задаем вопросы"""
    def __init__(self, main):
        self.entry_1 = Entry(main, width=3, font=15)
        self.btn_1 = Button(main, text="Проверить")
        self.label_1 = Label(main, width=27, font=15)

        self.entry_1.grid(row=0, column=0)
        self.btn_1.grid(row=0, column=1)
        self.label_1.grid(row=0, column=2)

        self.btn_1.bind("<Button-1>", self.answer)

    def answer(self, event):
        user_input = self.entry_1.get()

        try:
            if int(user_input) < 18:
                self.label_1["text"] = "Вам ещё рано сюда."
            else:
                self.label_1["text"] = "Добро пожаловать."
        except ValueError:
            self.label_1["text"] = "Введите корректный возраст."



tk = Tk()
tk.title("Сколько вам лет?")

q = Question(tk)


tk.mainloop()