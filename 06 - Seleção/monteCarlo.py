import turtle
import random

wn = turtle.Screen()
wn.setworldcoordinates(-1, -1, 1, 1)
fred = turtle.Turtle()
fred.up()

numdarts = 10
for i in range(numdarts):
    x = random.random() if random.randrange(2) == 0 else -random.random()
    y = random.random() if random.randrange(2) == 0 else -random.random()
    fred.goto(x, y)
    fred.stamp()

wn.exitonclick()
