# 3 lect https://www.youtube.com/watch?v=spin3l5XNiI&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=3

from tkinter import *

tk = Tk()

one = Label(tk, text="Один", bg="red", fg="yellow")
one.pack()

two = Label(tk, text="Два", bg="blue", fg="white")
two.pack(fill=X)

three = Label(tk, text="Три", bg="green", fg="purple")
three.pack(side=LEFT, fill=Y)

tk.mainloop()