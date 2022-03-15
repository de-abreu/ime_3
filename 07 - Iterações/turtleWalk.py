import random
import turtle


def isInScreen(w, t):
    leftBound = - w.window_width()/2
    rightBound = w.window_width()/2
    topBound = w.window_height()/2
    bottomBound = -w.window_height()/2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn


t = turtle.Turtle()
wn = turtle.Screen()
i = 0

t.shape('turtle')
while i < 4:
    angle = random.randrange(361)
    t.left(angle)
    t.forward(50)
    if not isInScreen(wn, t):
        t.forward(-50)
        i += 1
turtle.Terminator(wn)
