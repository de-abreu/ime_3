import sys


def isBinary(n):
    if (n < 0):
        return False
    while n > 0:
        if n % 10 > 1:
            return False
        n //= 10
    return True


def base10(n):
    if n // 10 == 0:
        return n % 10
    return base10(n // 10) * 2 + (n % 10)


def main():
    print("This program converts a number from base 10 to base 2.")

    try:
        n = int(input("Type a binary number and press ENTER: "))
    except ValueError:
        print("Error: not a number.")
        sys.exit()
    except EOFError:
        print("")
        sys.exit()
    if not isBinary:
        print("Not a binary number")
        sys.exit()
    print("The binary", n, "is equivalent to the decimal",
          base10(n), "in base 10.")


main()
