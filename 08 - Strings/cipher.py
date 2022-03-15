def cipher(message, key):
    cipher = ""

    for c in message:
        if c.islower():
            cipher += key[ord(c) - ord('a')]
        elif c.isupper():
            cipher += key[ord(c) - ord('A')].upper()
        else:
            cipher += c
    return cipher


def decipher(cipher, key):
    message = ""

    for c in cipher:
        if c.islower():
            message += chr(key.find(c) + ord('a'))
        elif c.isupper():
            message += chr(key.find(c.lower()) + ord('a')).upper()
        else:
            message += c
    return message


def main ():
    print("This program peforms a substitution cipher on non-accentuated letters.")

    key = "zoxyjdswgerkcaupmivthlbfqn"
    message = cipher(input("Input message: "), key)
    print("Encrypted message:", message)
    print("Decrypted message:", decipher(message, key))

main()
