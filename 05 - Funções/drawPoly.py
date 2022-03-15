import turtle

def drawPoly(turtle, sides, lenght):
    for i in range(sides):
        turtle.forward(lenght)
        turtle.left(360 / sides)

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

drawPoly(tess,
int(input("Dê o número de lados do polígono a ser desenhado: ")),
int(input("De o comprimento dos lados: ")))
        
wn.exitonclick()
