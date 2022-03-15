def piratefy(text):
    output = ""
    dict = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
            "boy": "matey", "madam": "proud beauty", "professor":
            "foul blaggart", "restaurant": "galley", "your": "yer", "excuse":
            "arr", "are": "be", "lawyer": "foul blaggart", "the": "th'",
            "restroom": "head", "my": "me", "hello": "avast", "is": "be",
            "man": "matey"}

    for word in text.split():
        output += " "
        lower = word.lower()
        if lower in dict:
            output += lower.capitalize() if word[0].isupper() else dict[lower]
        else:
            output += word
    return output.lstrip()


def main():
    print("This program translates common english to its pirate dialect equivalent.")
    translation = piratefy(input("Type in a message: "))
    print("Translation into pirate speak:", translation)


main()
