# 4 lect https://www.youtube.com/watch?v=hEYv0IK724U&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=4

from tkinter import *

tk = Tk()

label_1 = Label(tk, text="Имя")
label_2 = Label(tk, text="Пароль")

entry_1 = Entry(tk)
entry_2 = Entry(tk)

c = Checkbutton(tk, text="Остаться в системе")

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c.grid(columnspan=2)



tk.mainloop()