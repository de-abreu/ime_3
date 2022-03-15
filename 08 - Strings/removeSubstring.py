def removeSubstring(text, str):
    strlen = len(str)
    txtlen = len(text)
    i = 0

    while i < txtlen - strlen and text[i:i + strlen] != str:
        i += 1
    if i == txtlen - strlen:
        return text
    return text[0:i] + "█" * strlen + removeSubstring (text[i + strlen: txtlen], str)

print("This program removes a given string from a text.")

print("Resulting string: ", removeSubstring(
    input("Type in a text and press ENTER: "),
    input("Type in a string and press ENTER: ")
))
