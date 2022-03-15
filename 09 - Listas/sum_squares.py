import sys

def squaresSum(values):
    squares = []

    for i in values:
        try:
            squares.append(float(i) ** 2)
        except Exception:
            pass
    print("Squares:", squares)
    if len(squares) == 0:
        return -1
    return sum(squares)


def main ():
    print ("This program calculates the sum of squares of the numbers contained in a given list.")

    try:
        values = input("Type in values: ").split()
    except EOFError:
        print("")
        sys.exit()
    print("Values:", values)
    sum = squaresSum(values)
    if sum < 0:
        print("Error: No valid values present in the list.")
    else:
        print("Sum of squares:", sum)

main()
