''' Обработка событий нажатия на клавиатуру turtle
https://www.youtube.com/watch?v=OcDH_jFQ7yc&list=PLQAt0m1f9OHvowenYcOHrRP_v1VN-0TWF&index=6 '''
import turtle

speed = 5


def move_up():
    x, y = pen.position()
    pen.setposition(x, y + speed)


def move_down():
    x, y = pen.position()
    pen.setposition(x, y - speed)


def move_left():
    x, y = pen.position()
    pen.setposition(x - speed, y)


def move_right():
    x, y = pen.position()
    pen.setposition(x + speed, y)


def speed_up():
    global speed
    speed += 1
    print('Скорость:', speed)


def speed_down():
    global speed
    speed = max(1, speed - 1)
    print('Скорость:', speed)


def change():
    if pen.isvisible():
        pen.up()
        pen.hideturtle()
    else:
        pen.showturtle()
        pen.down()


window = turtle.Screen()
pen = turtle.Turtle()

window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(change, "space")
window.onkey(speed_up, "q")
window.onkey(speed_down, "w")

window.listen()  # Прослушивание
window.mainloop()  # Бесконечный цикл
