import turtle


def drawLSystem(t, lsystem):
    angle = 60

    for command in lsystem:
        if command == '+':
            t.left(angle)
        elif command == '-':
            t.right(angle)
        elif command == 'F':
            t.forward(10)


def simplifyLSystem(lsystem):
    return lsystem.replace("+-","").replace("-+","")


def SierpinskiTriangle(t, n):
    lsystem = "FAF--FF--FF"

    for i in range(n):
        tmp = ''
        for c in lsystem:
            if c == 'F':
                tmp += "FF"
            elif c == 'A':
                tmp += "-FAF++FAF++FAF--"
            else:
                tmp += c
        lsystem = tmp
    drawLSystem(t, simplifyLSystem(lsystem))

def initializeTurtle(t, wn):
    wn.setup(width = 510, height = 510)
    t.shape('turtle')
    t.pensize(3)
    t.up()
    t.goto(-250, -250)
    t.down()


def main():
    print("This program draws Sierpinski triangles.")

    try:
        n = int(input("Choose a level of complexity by giving a non-negative integer value: "))
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
    SierpinskiTriangle(t, n)
    wn.exitonclick()


main()
