import turtle

def drawStar(turtle, size):
    turtle.right(18)
    for i in range(1, 6):
        turtle.forward((-1) ** i * size)
        turtle.right(36)
    turtle.left(18)
    

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(1)

tess.left(90)
tess.up()
for i in range(5):
    tess.forward(350)
    tess.down()
    drawStar(tess, 100)
    tess.up()
    tess.forward(350)
    tess.right(36)

wn.exitonclick()
