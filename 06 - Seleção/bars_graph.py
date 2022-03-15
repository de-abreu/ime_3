import turtle


def drawBar(t, height):
    if height >= 200:
        t.color("#ec5f67")
        t.fillcolor("#ec5f67")
    elif height >= 100:
        t.color("#fac863")
        t.fillcolor("#fac863")
    elif height >= 0:
        t.color("#99c794")
        t.fillcolor("#99c794")
    else:
        t.color("#d8dee9")
        t.fillcolor("#343d46")

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write('  ' + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


xs = [48, 117, -200, 240, -160, 260, 220]  # aqui vão os dados
height = max(xs)
lenght = len(xs)
padding = 10

tess = turtle.Turtle()
tess.pensize(3)

wn = turtle.Screen()
wn.bgcolor("#d8dee9")
wn.setworldcoordinates(0 - padding, 0 - height, 40
                       * lenght + padding, height + padding)


for a in xs:
    drawBar(tess, a)

wn.exitonclick()
