"""Библиотека Tkinter - 14 - Диалоговые окна (3/3)
https://www.youtube.com/watch?v=YX0yggSH7pE&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=14 """

from tkinter.filedialog import *
from tkinter import *

def open_file():
    of = askopenfilename()
    file = open(of, "r")
    txt.insert(END, file.read())
    file.close()

def save_file():
    sf = asksaveasfilename()
    final_text = txt.get(1.0, END)
    file = open(sf, "w")
    file.write(final_text)
    file.close()

def exit_file():
    tk.quit()

tk = Tk()

main_menu = Menu(tk)
tk.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=first_item)

first_item.add_command(label="Open", command=open_file)
first_item.add_command(label="Save", command=save_file)
first_item.add_command(label="Exit", command=exit_file)

txt = Text(tk, width=40, height=15, font=12)
txt.pack(expand=YES, fill=BOTH)

tk.mainloop()