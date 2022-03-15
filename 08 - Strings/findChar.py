def findChar(string, char):
    """
      Find and return the index of char in string,
      otherwise return -1 if not found.
    """

    index = -1
    for i in range(len(string)):
        if string[i] == char:
            index = i
            break
    return index


print(findChar("Compsci", "p"))
print(findChar("Compsci", "C"))
print(findChar("Compsci", "i"))
print(findChar("Compsci", "x"))
