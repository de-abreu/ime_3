import turtle

def drawStar(turtle, points, size):
    angle  = 360 / (points * 2)
    turtle.right(angle / 2)
    for i in range(1, points + 1):
        turtle.forward((-1) ** i * size)
        turtle.right(angle)
    turtle.left(angle/2)
    

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

drawStar(tess, int(input("Quantas pontas? ")), 100)


wn.exitonclick()
