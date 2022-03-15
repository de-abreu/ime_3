import turtle

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

tess.right(90)
for i in range(121):
    tess.forward(i * 6)
    tess.right(108)
        
wn.exitonclick()
