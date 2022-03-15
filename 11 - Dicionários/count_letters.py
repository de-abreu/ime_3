def countLetters(text, case_insensitive):
    letterCount = dict()
    if case_insensitive == "y" or case_insensitive == "yes":
        for c in text.lower():
            letterCount[c] = letterCount.get(c, 0) + 1
    else:
        for c in text:
            letterCount[c] = letterCount.get(c, 0) + 1
    return letterCount


def main():
    print("This program counts how many characters of each distinct character is present in a given text.")
    case_insensitive = input(
        "Should this count be case insenstitive? (y)es / (n)o: ").lower()
    letterCount = countLetters(
        input("Type in a given text: "), case_insensitive)
    for c in sorted(letterCount):
        print(c, ":", letterCount[c])


main()
