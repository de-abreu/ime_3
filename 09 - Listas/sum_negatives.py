import sys

def sumNegatives(values):
    sum = 0

    for i in values:
        try:
            value = int(i)
        except Exception:
            continue
        if value < 0:
            sum += value
    return sum


def main():
    print ("This program calculates the sum of negative numbers in a given list.")

    try:
        values = input("Type in values and press ENTER: ").split()
    except EOFError:
        print("")
        sys.exit()
    print("Sum of negatives:", sumNegatives(values))

main()
