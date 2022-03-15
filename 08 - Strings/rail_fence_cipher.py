import random


def cycleLength(rail, index, railCount, cycle):
    if rail == 0:
        return 2 * (railCount - (rail + 1))
    if rail == railCount - 1:
        return 2 * rail
    if rail == index:
        return 2 * (railCount - (rail + 1))
    if cycle == 2 * (railCount - (rail + 1)):
        return 2 * rail
    return 2 * (railCount - (rail + 1))


def railFenceCipher(message, length, rails):
    cycle = 0
    cipher = ""

    for j in range(rails):
        k = j
        while True:
            cipher += message[k]
            cycle = cycleLength(j, k, rails, cycle);
            k += cycle
            if k >= length:
                break;
    return cipher


def railFenceDecipher(cipher, length, rails):
    i = cycle = 0
    message = [None] * length

    for j in range(rails):
        k = j
        while True:
            message[k] = cipher[i]
            cycle = cycleLength(j, k, rails, cycle);
            k += cycle
            i += 1
            if k >= length:
                break;
    return "".join(message)


def main ():
    print("This program allows for one to encrypt a message using the Rail Fence Cipher.")

    message = input("Type in a message with 3 characters or more to be encrypted: ")
    length = len(message)

    if length < 3:
        print("Error: message too short to be encrypted.")
        return

    # rails = 2 if length // 3 < 3 else random.randrange(2, length // 3)
    rails = 5
    cipher = railFenceCipher(message, length, rails)
    print("Encrypted message:", cipher)
    print("Decrypted message:", railFenceDecipher(cipher, length, rails))


main()
