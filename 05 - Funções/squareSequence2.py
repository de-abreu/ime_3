import turtle

def drawSquare(turtle, side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def drawCenteredSquare(turtle, x, y, side):
    turtle.up()
    turtle.goto(-side/2, -side/2)
    turtle.down()
    drawSquare(turtle, side)

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

for i in range(5):
    drawCenteredSquare(tess, 0, 0, 20 * (i + 1))
        
wn.exitonclick()
