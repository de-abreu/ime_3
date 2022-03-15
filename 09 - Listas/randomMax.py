import sys
import random

def maximum(values):
    maximum = values[0]

    for i in range(1, len(values)):
        if values[i] > maximum:
            maximum = values[i]
    return maximum


def main ():
    print ("This program calculates the maximum value of a given quantity of random numbers between 0 and 1000.")

    try:
        n = int(input("Type a quantity: "))
    except ValueError:
        print("Error: Not an integer value.")
        sys.exit()
    except EOFError:
        print("")
        sys.exit()
    if n < 0:
        print("Error: negative value.")
        sys.exit()

    values = [random.randrange(1,1000) for i in range(n)]
    print("Values:", values)
    print("Maximum:", maximum(values))

main()
