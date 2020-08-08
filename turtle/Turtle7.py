"""Рисуем олимпийские кольца Turtle
https://www.youtube.com/watch?v=PuMkCrRmWV0&list=PLQAt0m1f9OHvowenYcOHrRP_v1VN-0TWF&index=7"""

import turtle

window = turtle.Screen()
r = 100

europe = turtle.Turtle()
africa = turtle.Turtle()
america = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europe, africa, america, asia, australia]:
    i.up()
    i.hideturtle()

europe.color('blue')
africa.color('black')
america.color('red')
asia.color('yellow')
australia.color('green')

europe.goto(-2 * r, r*0.5)
africa.goto(0, r*0.5)
america.goto(2 * r, r*0.5)
asia.goto(-r, -r*0.5)
australia.goto(r, -r*0.5)

for i in [europe, africa, america, asia, australia]:
    i.down()
    i.speed(0)
    i.pensize(r/6)
    i.circle(r-r/8)


window.mainloop()
