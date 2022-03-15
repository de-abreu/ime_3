import sys

def countOdds(values):
    odds = 0

    for i in values:
        try:
            value = int(i)
        except Exception:
            continue
        if value % 2 != 0:
            odds += 1
    return odds


def main():
    print ("This program calculates the quantity of Odd numbers in a given list of numbers.")

    try:
        values = input("Type in values: ").split()
    except EOFError:
        print("")
        sys.exit()
    print(countOdds(values), "odd values.")

main()
