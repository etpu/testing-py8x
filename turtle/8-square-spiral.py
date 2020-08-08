import turtle

"""Нарисуйте «квадратную» спираль. """

paws = 6

while True:
    # turtle.speed(10)
    turtle.shape('turtle')
    turtle.pendown()
    for i in range(10, 330, 10):
        turtle.forward(i)
        turtle.left(90)
    turtle.penup()
    turtle.goto(0, 0)