import turtle


def solve(mystery, t):
    for line in mystery.readlines():
        line = line.split()
        if line[0] == "CIMA":
            t.up()
        elif line[0] == "BAIXO":
            t.down()
        else:
            t.goto(int(line[0]), int(line[1]))
    mystery.close()


def main():
    print("This program solves a mystery! Uuuuhh!")
    mystery = input("Type in the path of the misterious file: ")

    wn = turtle.Screen()
    t = turtle.Turtle()
    t.shape('turtle')
    t.pensize(3)
    solve(open(mystery, 'r'), t)
    wn.exitonclick()


main()
