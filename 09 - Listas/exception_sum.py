import sys


def exceptionSum(values):
    sum = 0
    pair_found = False

    for i in values:
        try:
            value = float(i)
        except Exception:
            continue
        if not pair_found and value % 2 == 0:
            pair_found = True
        else:
            sum += value
    return sum


def main():
    print ("This program sums all numbers given, except for the first pair number.")

    try:
        values = input("Type in values: ").split()
    except EOFError:
        print("")
        sys.exit()
    print("Sum:", exceptionSum(values))


main()
