import sys


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("This program displays the nth number in the fibonacci sequence.")

    try:
        n = int(input("Type in a value for n and press ENTER: "))
    except ValueError:
        print("Error: not a number.")
        sys.exit()
    except EOFError:
        print("")
        sys.exit()
    if n < 0:
        print("Error: negative value.")
        sys.exit()

    print(fibonacci(n))


main()
