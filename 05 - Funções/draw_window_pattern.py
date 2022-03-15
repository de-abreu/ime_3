import turtle

def drawSquare(turtle, side):
    for i in range(4):
        turtle.left(90)
        turtle.forward(side)

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

for i in range(19):
    drawSquare(tess, 50)
    tess.left(18)
        
wn.exitonclick()
