import tkinter as tk
from random import randint

WIDTH = 380
HEIGHT = 260

def canvas_click_handler(event):
    print(f'Hello World! {event.x=}, {event.y=}')

def tick():
    global x, y, ball_id
    print("move")
    x += 1
    y += 1
    canvas.move(ball_id, +1, +1)
    root.after(50, tick)

def main():
    global root, canvas
    global ball_id, x, y, R
    root = tk.Tk()
    canvas = tk.Canvas(root)
    root.geometry(f'{WIDTH}x{HEIGHT}')
    canvas.pack(anchor="nw")
    canvas.bind('<Button-1>', canvas_click_handler)

    R = randint(2, 80)
    x = randint(R, WIDTH - R)
    y = randint(R, HEIGHT - R)


    ball_id = canvas.create_oval(x - R, y - R, x + R, y + R, fill='green')
    tick()

    root.mainloop()


if __name__ == "__main__":
    main()
