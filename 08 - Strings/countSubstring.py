def countSubstring(str, substr):
    length = len(substr)
    count = 0
    str = str.lower()
    substr = substr.lower()

    for i in range(len(str) - length):
        if str[i:i + length] == substr:
            count += 1
    return count


print("This program counts the occurences of a given substring in a string, while being case insensitive.")

str = input("Type in a string and press ENTER: ")
substr = input("Type in a substring and press ENTER: ")

print("The substring \"" + substr + "\" appears",
      countSubstring(str, substr), "times in the given text.")
