import sys

def substituteString(source, pattern, length, substitute):
    str = source.lower()
    try:
        i = str.index(pattern)
    except Exception:
        return source
    return source[:i] + substitute + substituteString(source[i + length:], pattern, length, substitute)



def main():
    print ("This program substitutes a substring for another in a given string (case insensitive)")

    source = input("Type in a string: ")
    pattern = input("Type a substring to be substituted: ").lower()
    length = len(pattern)
    substitute = input("Type its substitute: ")

    print(substituteString(source, pattern, length, substitute))


main()
