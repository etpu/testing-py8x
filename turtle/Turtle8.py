"""Как задать случайный цвет turtle
https://www.youtube.com/watch?v=SrTFTJr062c&list=PLQAt0m1f9OHvowenYcOHrRP_v1VN-0TWF&index=8"""

import random
import time
import turtle


def choose_random_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue


window = turtle.Screen()

bob = turtle.Turtle()
bob.speed(0)
bob.pensize(20)

for i in range(360):
    bob.color(choose_random_color())
    bob.forward(2)
    bob.left(1)

# while True:
#     window.bgcolor(choose_random_color())
#     time.sleep(0.5)
