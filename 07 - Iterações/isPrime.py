import sys


def approximateSqrt(n):
    suplim = n
    inflim = 1

    while True:
        root = (suplim + inflim) / 2
        square = root ** 2

        if square < n - 1:
            inflim = root
        elif square < n + 1:
            return int(root)
        else:
            suplim = root


def isPrime(n):
    if n != 2:
        if n < 2 or n % 2 == 0:
            return False

        limit = approximateSqrt(n) + 2
        for i in range(3, limit, 2):
            if (n % i == 0):
                return False
    return True


print("This program asserts if a given no negative integer number is prime.")
try:
    n = int(input("Type a given integer value: "))
except ValueError:
    print("Error: not a number.")
    sys.exit()
except EOFError:
    print("")
    sys.exit()
if n < 0:
    print("Error:", n, "is negative.")
    sys.exit()
if isPrime(-n if n < 0 else n):
    print(n, "is prime")
else:
    print(n, "is not prime")
