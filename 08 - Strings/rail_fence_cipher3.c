#include <stdlib.h>
#include <locale.h>
#include <wchar.h>
#include <stdio.h>

int randRange(int min, int max) {
    return rand() % (max + 1 - min) + min;
}

wchar_t * readString(int * length) {
    int i = 0, size = 1;
    wchar_t c, *input = malloc(sizeof(wchar_t));

    while ((c = getwchar()) != WEOF && c != '\n') {
        if (i == size - 1) {
            size *= 2;
            input = realloc(input, size * sizeof(input));
        }
        input[i++] = c;
    }
    input[i] = '\0';
    *length = i;
    return input;
}

int cycleLength(int rail, int railIndex, int rails, int cycle) {
    if (rail == 0)
        return 2 * (rails - (rail + 1));
    if (rail == rails - 1)
        return 2 * rail;
    if (rail == railIndex)
        return 2 * (rails - (rail + 1));
    if (cycle == 2 * (rails - (rail + 1)))
        return 2 * rail;
    return 2 * (rails - (rail + 1));
}

wchar_t * railFenceCipher(wchar_t *message, int length, int rails) {
    int i, j, k, cycle;
    wchar_t *cipher = malloc(length * sizeof(wchar_t));

    for (i = k = 0; i < rails; i++) {
        j = i;
        do {
            cipher[k++] = message[j];
            cycle = cycleLength(i, j, rails, cycle);
            j += cycle;
        } while (j < length);
    }
    cipher[k] = '\0';
    return cipher;
}

wchar_t * railFenceDecipher(wchar_t *cipher, int length, int rails) {
    int i, j, k, cycle;
    wchar_t *message = malloc(length * sizeof(wchar_t));

    for (i = k = 0; i < rails; i++) {
        j = i;
        do {
            message[j] = cipher[k++];
            cycle = cycleLength(i, j, rails, cycle);
            j += cycle;
        } while (j < length);
    }
    message[k] = '\0';
    return message;
}

int main () {
    setlocale(LC_ALL, "pt_BR.UTF-8");
    wchar_t *message, *cipher;
    int length, rails;

    printf("This program allows for one to encrypt a message using the Rail Fence Cipher.\nType in a message with 3 characters or more to be encrypted: ");

    message = readString(&length);

    if (length < 3) {
        printf("Error: Message too short to be encrypted.\n");
        return 1;
    }

    rails = (length / 3 < 3) ? 2 : randRange(2, length / 3);
    cipher = railFenceCipher(message, length, rails);
    printf("Encrypted message: %ls\n", cipher);
    free(message);
    message = railFenceDecipher(cipher, length, rails);
    printf("Decrypted message: %ls\n", message);
    free(message);
    free(cipher);
    return 0;
}
