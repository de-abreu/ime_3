def printTriangular(n):
    """Print a list of triangular numbers and their indices"""

    print("Index", '\t', "Triangular number")
    print("-----", '\t', "-----------------")

    for i in range(1, n + 1):
        print(i, '\t', i * (i + 1) // 2)


print("This program prints the first n triangular numbers.")

try:
    n = int(input("Type a value for n and press ENTER: "))
except ValueError:
    print("Error: n is not an integer.")
    exit()
except EOFError:
    print("")
    exit()
if n < 0:
    print("Error: n has negative value.")
    exit()

printTriangular(n)
