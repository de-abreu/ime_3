import string


def findLongest(file):
    longestLength = 0
    longestWords = []
    word = ""
    length = 0

    for c in file.read():
        if c in string.ascii_letters + "-":
            word += c
            length += 1
        else:
            if length > longestLength:
                longestWords = [word]
                longestLength = length
            elif length == longestLength and not word in longestWords:
                longestWords.append(word)
            word = ""
            length = 0
    return (longestWords, longestLength)


def main():
    print("This program finds the longest word, or words, in a plain text file.")
    file = open(input("Type in a file's path: "), 'r')
    longestWords = findLongest(file)
    if len(longestWords[0]) == 1:
        print("The longest word in the given file is "
              + longestWords[0] + ", with a length of", longestWords[1], "characters")
    else:
        print("The longest words in the given file are:",
              longestWords[0][0], end='')
        for word in longestWords[0][1:]:
            print(',', word, end='')
        print("\nAll with a length of", longestWords[1], "characters")
    file.close()


main()
