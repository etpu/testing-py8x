import turtle

"""Нарисуйте 10 вложенных квадратов."""

while True:
    turtle.shape('turtle')
    for x in range(10, 110, 10):
        turtle.penup()
        turtle.goto(-x/2, -x/2)
        turtle.pendown()
        for i in range(4):
            turtle.forward(x)
            turtle.left(90)