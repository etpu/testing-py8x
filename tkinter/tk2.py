# 2 lect https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2

from tkinter import *

tk = Tk()

top_frame = Frame(tk)
top_frame.pack()

bottom_frame = Frame(tk)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Кнопка1", fg="red")
button2 = Button(top_frame, text="Кнопка2", fg="blue")
button3 = Button(top_frame, text="Кнопка3", fg="brown")
button4 = Button(bottom_frame, text="Кнопка4", fg="green")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

tk.mainloop()