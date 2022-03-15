import sys


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def main():
    print("This program calculates the factorial for a non-negative integer.")

    try:
        n = int(input("Type in a number and press ENTER: "))
    except ValueError:
        print("Error: not a number.")
        sys.exit()
    except EOFError:
        print("")
        sys.exit()
    if n < 0:
        print("Error: negative value.")
        sys.exit()

    print(str(n) + "! =", factorial(n))


main()
