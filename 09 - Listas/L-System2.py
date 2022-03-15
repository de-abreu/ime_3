import turtle


def draw_l_system(lsystem, t):
    saveStates = []

    for command in lsystem:
        if command == '+':
            t.left(25)
        elif command == '-':
            t.right(25)
        elif command == 'F':
            t.forward(10)
        elif command == '[':
            saveStates.append([t.heading(),t.xcor(),t.ycor()])
        elif command == ']':
            state = saveStates.pop()
            t.setheading(state[0])
            t.setposition(state[1],state[2])


def initialize_l_system(n):
    lsystem = 'F'

    for i in range(n):
        tmp = ""
        for c in lsystem:
            if c == 'F':
                tmp += "F[-F]F[+F]F"
            else:
                tmp += c
        lsystem = tmp
    return lsystem


def main():
    print("This program draws an L-System.")

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
    t.shape('turtle')
    t.pensize(3)
    lsystem = initialize_l_system(n)
    print(lsystem)
    draw_l_system(lsystem, t)
    wn.exitonclick()

main()
