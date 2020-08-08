"""Прыгающий мячик Bounce ball
https://www.youtube.com/watch?v=nGDCPL5TE2Y&list=PLQAt0m1f9OHvowenYcOHrRP_v1VN-0TWF&index=9"""
import random
import turtle

border_x = 300
border_y = 300
border_size = 5

window = turtle.Screen()
border = turtle.Turtle()
border.color('red')
border.speed(0)
border.pensize(border_size)
border.hideturtle()
border.up()
border.goto(border_x, border_y)
border.down()
border.goto(border_x, -border_y)
border.goto(-border_x, -border_y)
border.goto(-border_x, border_y)
border.goto(border_x, border_y)

ball = turtle.Turtle()
ball.shape('circle')

rand_x = random.randint(-border_x + border_size, border_x - border_size)
rand_y = random.randint(-border_y + border_size, border_y - border_size)

dx = 4
dy = 5

while True:
    x, y = ball.position()
    if x + dx >= border_x - border_size or x + dx <= -border_x + border_size:
        dx = -dx
    if y + dy >= border_y - border_size or y + dy <= -border_y + border_size:
        dy = -dy
    ball.goto(x + dx, y + dy)

window.mainloop()
