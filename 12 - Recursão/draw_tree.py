import turtle
import random


def tree(branchLen, t):
    if branchLen < 5:
        return
    t.color("#bdcebe" if branchLen < 45 else "#b9936c")
    t.pensize(branchLen // 5)
    t.forward(branchLen)
    angle = random.randrange(14, 47, 2)
    length = random.randrange(branchLen - 10, branchLen)
    t.right(angle // 2)
    tree(length, t)
    t.left(angle)
    tree(length, t)
    t.right(angle // 2)
    t.color("#bdcebe" if branchLen < 45 else "#b9936c")
    t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t)
    myWin.exitonclick()


main()
