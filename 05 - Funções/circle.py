import turtle

def drawCircle (screen, centre_x, centre_y, radius)
    cursor = turtle.Turtle()

    cursor.left(90)
    cursor.up()

    // Draw upper arch
    cursor.goto(centre_x - radius, centre_y)
    cursor.down()
    for x in range(-radius, radius + 1):
        cursor.goto(centre_x + x, )


wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tess = turtle.Turtle()
tess.color("hotpink")

sides = int(input("Digite o número de lados do polígono regular: "))

for i in range(sides):
    tess.forward(100)
    tess.left(360 / sides)

wn.exitonclick()
