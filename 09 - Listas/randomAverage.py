import sys
import random

def average(values):
    return 0 if len(values) == 0 else sum(values) / len(values)


def main ():
    print ("This program calculates the average of a given quantity of random numbers between 0 and 1000.")

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
    print("Average:", average(values))

main()
