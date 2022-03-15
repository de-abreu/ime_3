import unidecode


def normalizeString(str):
    """Remove from the string whitespaces, accents, punctuation, and make it lowercase only."""

    normalized = ""
    for c in str:
        if c.isalnum():
            normalized += unidecode.unidecode(c.lower())
    return normalized


def isPalindrome(str):
    str = normalizeString(str)
    length = len(str)

    for i in range(length // 2):
        if str[i] != str[length - 1 - i]:
            return False
    return True


print("This program evaluates if a given word or sentence is a palidrome.")

if isPalindrome(input("Type in a word or sentence and press ENTER: ")):
    print("That's a palidrome.")
else:
    print("That's not a palindrome")
