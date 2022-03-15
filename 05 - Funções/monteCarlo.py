import turtle
import random

wn = turtle.Screen()
wn.setworldcoordinates(-1, -1, 1, 1)
fred = turtle.Turtle()
fred.speed(0)
fred.left(90)
fred.up()

numdarts = 1000
q = 0
d = 0
for i in range(numdarts):
    x = random.random() if random.randrange(2) == 0 else -random.random()
    y = random.random() if random.randrange(2) == 0 else -random.random()
    fred.goto(x, y)
    fred.stamp()
    if fred.distance(0, 0) <= 1:
        q += 1
    d += 1

print("Valor aproximado de π para", numdarts, "dardos: ", 4 * q/d)
wn.exitonclick()
