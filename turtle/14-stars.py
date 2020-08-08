import turtle, time
"""Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами."""

top = 6
turtle.shape('turtle')
turtle.speed(1)

def hard_star(top):
    for i in range(top):
        turtle.forward(200)
        turtle.right(180-(180/(top)))
    for i in range(top):
        turtle.forward(200)
        turtle.right(180-(180/(top)))

if top % 2 == 0:
    top //= 2
    if top//2%2 != 0:
        hard_star(top)

else:
    while True:
        for i in range(top):
            turtle.forward(200)
            turtle.left(180-(180/top))
