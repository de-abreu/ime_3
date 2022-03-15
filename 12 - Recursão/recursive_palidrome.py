import unidecode


def normalizeString(str):
    """Remove from the string whitespaces, accents, punctuation, and make it lowercase only."""

    normalized = ""
    for c in str:
        if c.isalnum():
            normalized += unidecode.unidecode(c.lower())
    return normalized


def reverseString(str, len):
    last = len - 1
    if last == 0:
        return str[last]
    return str[last] + reverseString(str[:last])


def isPalindrome(str):
    str = normalizeString(str)
    if str == reverseString(str, len(str)):
        return True
    return False


print("This program evaluates if a given word or sentence is a palidrome.")

if isPalindrome(input("Type in a word or sentence and press ENTER: ")):
    print("That's a palidrome.")
else:
    print("That's not a palindrome")
