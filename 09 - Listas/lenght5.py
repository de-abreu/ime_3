import sys

def matchLength(words, length):
    count = 0

    for word in words:
        if len(word) == length:
            count += 1
    return count


def main():
    print ("This program calculates the number of words in a given text that have a given length.")

    try:
        length = int(input("Type in the desired length: "))
    except ValueError:
        print("Error: Not an integer value.")
        sys.exit()
    except EOFError:
        print("")
        sys.exit()
    if length < 0:
        print("Error: negative value.")
        sys.exit()

    try:
        words = input("Type in the text: ").split()
    except EOFError:
        print("")
        sys.exit()
    print("Number of words with length " + str(length) + ":", matchLength(words, length))

main()
