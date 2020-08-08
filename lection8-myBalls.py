import tkinter
from random import randint

WIDTH = 800
HEIGHT = 600
colors = ["green", "red", "purple", "black", "brown", "pink", "blue", "magenta", "yellow"]


class Ball:
    def __init__(self):
        self.R = randint(10, 60)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (randint(+1, +40), randint(+1, +40))
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=colors[randint(0, 8)])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def canvas_click_handler(event):
    print(f'Hello World! {event.x=}, {event.y=}')

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    tk.after(50, tick)


def main():
    global tk, canvas, balls
    tk = tkinter.Tk()
    canvas = tkinter.Canvas(tk, width=WIDTH+20, height=HEIGHT+20)
    tk.geometry(f'{WIDTH+20}x{HEIGHT+20}')
    # btn = tkinter.Button(tk, text='Ускорение!!!!', command=tick)
    # btn.pack()
    canvas.pack(anchor="se")
    canvas.bind('<Button-1>', canvas_click_handler)
    balls = [Ball() for i in range(5)]
    tick()
    tk.mainloop()


if __name__ == "__main__":
    main()
