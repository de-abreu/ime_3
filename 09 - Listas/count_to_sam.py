import sys

def countToSam(words):
    count = 0

    for word in words:
        count += 1
        if word == "sam":
            return count
    return count


def main():
    print ("This program counts the number of words until the end of the text or the occurence of the word \"sam\" (??)")

    try:
        words = input("Type in the text: ").split()
    except EOFError:
        print("")
        sys.exit()
    print("Word count:", countToSam(words))

main()
