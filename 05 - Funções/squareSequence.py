import turtle

def drawSquare(turtle, side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

for i in range(5):
    drawSquare(tess, 20)
    tess.up()
    tess.forward(40)
    tess.down()
        
wn.exitonclick()
