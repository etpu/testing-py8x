import turtle

"""Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный многоугольник 
с большим числом сторон будет выглядеть как окружность. """

while True:
    turtle.shape('turtle')
    for x in range(365):
        turtle.forward(1)
        turtle.left(1)
    # turtle.circle(50) # https://docs.python.org/3/library/turtle.html#turtle.circle
