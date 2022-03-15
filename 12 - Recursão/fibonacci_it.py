import sys


def fibonacci(n):
    i = 0
    mem = [1, 1, 1]

    while i < n and i < 2:
        i += 1
    while n > 2:
        mem[i - 2] = mem[i - 1]
        mem[i - 1] = mem[i]
        mem[i] += mem[i - 2]
        n -= 1
    return mem[i]


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
