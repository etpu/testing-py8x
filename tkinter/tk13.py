"""Библиотека Tkinter - 12 - Диалоговые окна (2/3)
https://www.youtube.com/watch?v=dHiqSj910J4&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=13 """

from tkinter import *
from tkinter.messagebox import *

def ask_question(event):
    answer = askquestion("AskQuestion", "Вопрос первый")
    label_1.configure(text=answer)

def ask_ok(event):
    answer = askokcancel("AskOkCancel", "Вопрос второй")
    label_2.configure(text=answer)

def ask_yn(event):
    answer = askyesno("AskYesNo", "Вопрос третий")
    label_3.configure(text=answer)

def ask_rc(event):
    answer = askretrycancel("AskRetryCancel", "Вопрос четвертый")
    label_4.configure(text=answer)



tk = Tk()

btn_1 = Button(tk, text="askquestion", font=("Ubuntu", 20), width=12)
btn_1.grid(row=0, column=0, sticky="ew")
label_1 = Label(tk, font=("Ubuntu", 20), width=12)
label_1.grid(row=0, column=1)
btn_1.bind("<Button-1>", ask_question)

btn_2 = Button(tk, text="askokcancel", font=("Ubuntu", 20), width=12)
btn_2.grid(row=1, column=0, sticky="ew")
label_2 = Label(tk, font=("Ubuntu", 20), width=12)
label_2.grid(row=1, column=1)
btn_2.bind("<Button-1>", ask_ok)

btn_3 = Button(tk, text="askyesno", font=("Ubuntu", 20), width=12)
btn_3.grid(row=2, column=0, sticky="ew")
label_3 = Label(tk, font=("Ubuntu", 20), width=12)
label_3.grid(row=2, column=1)
btn_3.bind("<Button-1>", ask_yn)

btn_4 = Button(tk, text="askretrycancel", font=("Ubuntu", 20), width=12)
btn_4.grid(row=3, column=0, sticky="ew")
label_4 = Label(tk, font=("Ubuntu", 20), width=12)
label_4.grid(row=3, column=1)
btn_4.bind("<Button-1>", ask_rc)



tk.mainloop()