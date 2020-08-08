""" Библиотека Tkinter - 8 - Секундомер
https://www.youtube.com/watch?v=F-TAPB87vCU&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=8 """

# Не работает

from tkinter import *

temp_seconds = 0
after_id = ''

def tick():
    global temp_seconds, after_id
    after_id = tk.after(1000, tick())  # RecursionError: maximum recursion depth exceeded
    label_1.configure(text=str(temp_seconds))
    temp_seconds += 1

def start_sw():
    btn_1.grid_forget()
    btn_2.grid(row=1, columnspan=2, sticky="ew")
    tick()

tk = Tk()

tk.title("Stopwatch")

label_1 = Label(tk, width=5, font=("Ubuntu", 100), text="00:00")
label_1.grid(row=0, columnspan=2)

btn_1 = Button(tk, text="Start", font=("Ubuntu", 30), command=start_sw)
btn_2 = Button(tk, text="Stop", font=("Ubuntu", 30))
btn_3 = Button(tk, text="Continue", font=("Ubuntu", 30))
btn_4 = Button(tk, text="Reset", font=("Ubuntu", 30))

btn_1.grid(row=1, columnspan=2, sticky="ew")

tk.mainloop()