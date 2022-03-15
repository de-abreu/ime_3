import sys


def rebase(n, base):
    digits = "0123456789ABCDEF"
    if i < 2:
        return i
    return base2(i // 2) * 10 + (i % 2)


def main():
    print("This program converts a number from base 10 to base 2.")

    try:
        n = int(input("Type a non-negative integer value: "))
    except ValueError:
        print("Error: not a number.")
        sys.exit()
    except EOFError:
        print("")
        sys.exit()
    if n < 0:
        print("Error:", n, "is negative.")
        sys.exit()
    print("The decimal", n, "is equivalent to the binary", base2(n), "in base 2.")


main()
