import turtle

"""Нарисуйте паука с n лапами. Пример n = 12:"""

paws = 60

while True:
    turtle.shape('turtle')
    for x in range(paws):
        turtle.left(360/paws)
        turtle.forward(100)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(100)
        turtle.left(180)