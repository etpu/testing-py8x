"""Библиотека Tkinter - 12 - Диалоговые окна (1/3)
https://www.youtube.com/watch?v=Qzx_NnUv0DU&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=12 """

from tkinter import *
from tkinter.messagebox import *

tk = Tk()

btn_1 = Button(tk, text="Info", font=("Ubuntu", 20), comman=lambda: showinfo("Showinfo", "Информация"))
btn_1.grid(row=0, column=0, sticky="ew")

btn_2 = Button(tk, text="Warning", font=("Ubuntu", 20), comman=lambda: showwarning("ShowWarning", "Предупреждение"))
btn_2.grid(row=1, column=0, sticky="ew")

btn_3 = Button(tk, text="Error", font=("Ubuntu", 20), comman=lambda: showerror("ShowError", "Ошибка"))
btn_3.grid(row=2, column=0, sticky="ew")

tk.mainloop()