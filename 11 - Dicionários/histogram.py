import turtle


def countLetters(text):
    letterCount = dict()
    for c in text:
        letterCount[c] = letterCount[c] + 1 if c in letterCount else 1
    return letterCount


def drawBar(t, c, value, max):
    percent = value / max * 100

    if percent > 75:
        t.color("#ec5f67")
        t.fillcolor("#ec5f67")
    elif percent > 25:
        t.color("#fac863")
        t.fillcolor("#fac863")
    else:
        t.color("#99c794")
        t.fillcolor("#99c794")

    t.begin_fill()
    t.left(90)
    t.forward(value)
    t.write(" \"" + c + "\": " + str(value), font=("Roboto", 10, ""))
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(value)
    t.left(90)
    t.end_fill()


def drawHistogram(letterCount):
    letters = sorted(letterCount.keys())
    height = max(letterCount.values())
    length = len(letters)
    padding = 10
    t = turtle.Turtle()
    t.pensize(3)
    wn = turtle.Screen()
    wn.bgcolor("#d8dee9")
    wn.setworldcoordinates(0 - padding, 0 - height, 40
                           * length + padding, height + padding)

    for c in letters:
        drawBar(t, c, letterCount[c], height)
    wn.exitonclick()


def main():
    print("This program counts how many characters of each distinct character is present in a given text, and draws an histogram from it.")
    drawHistogram(countLetters(input("Type in a given text: ")))


main()
