import turtle


def drawLSystem(t, lsystem):
    if lsystem == "":
        return
    if lsystem[0] == '+':
        t.left(90)
    elif lsystem[0] == '-':
        t.right(90)
    elif lsystem[0] == 'F':
        t.forward(50)
    drawLSystem(t, lsystem[1:])


def simplifyLSystem(lsystem):
    return lsystem.replace("+-", "").replace("-+", "")


def HilbertCurve(t, n):
    lsystem = 'A'

    for i in range(n):
        tmp = ""
        for c in lsystem:
            if c == 'A':
                tmp += "+BF-AFA-FB+"
            elif c == 'B':
                tmp += "-AF+BFB+FA-"
            else:
                tmp += c
        lsystem = tmp
    drawLSystem(t, simplifyLSystem(lsystem))


def initializeTurtle(t, wn):
    wn.setup(width=510, height=510)
    t.shape('turtle')
    t.pensize(3)
    t.up()
    t.goto(-250, -250)
    t.down()


def main():
    print("This program draws Hilbert curves.")

    try:
        n = int(
            input("Choose a level of complexity by giving a non-negative integer value: "))
    except ValueError:
        print("Error: n is not an integer.")
        exit()
    except EOFError:
        print("")
        exit()
    if n < 0:
        print("Error: n has negative value.")
        exit()

    wn = turtle.Screen()
    t = turtle.Turtle()
    initializeTurtle(t, wn)
    HilbertCurve(t, n)
    wn.exitonclick()


main()
