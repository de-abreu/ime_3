#include <stdlib.h>
#include <locale.h>
#include <wchar.h>
#include <stdio.h>
#include <stdbool.h>

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

int ceil (int n, int d) {
    return 1 + (n - 1) / d;
}

int cycleLength(int rail, int railIndex, int rails, int cycle) {
    if (rail == 0)
        return cycle = 2 * (rails - (rail + 1));
    if (rail == rails - 1)
        return cycle = 2 * rail;
    if (rail == railIndex)
        return cycle = 2 * (rails - (rail + 1));
    else if (cycle == 2 * (rails - (rail + 1)))
        return cycle = 2 * rail;
    return cycle = 2 * (rails - (rail + 1));
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

wchar_t popFirst (wchar_t *str) {
    int i;
    wchar_t c = str[0];

    for (i = 0; str[i] != '\0'; i++)
        str[i] = str[i + 1];
    return c;
}

void freeRails(wchar_t **rails, int n) {
    int i;

    for (i = 0; i < n; i++)
        free(rails[i]);
    free(rails);
}

wchar_t * railFenceDecipher(wchar_t *cipher, int length, int n) {
    int i, j, k, counter, cycle;
    wchar_t **rails = malloc(n * sizeof(wchar_t*)),
    *message = malloc(length * sizeof(wchar_t));
    bool forward = true;

    for (i = j = 0; i < n; i++) {
        k = 0;
        counter = i;
        rails[i] = malloc((ceil(length, n - 1) + 1) * sizeof(wchar_t));
        while (counter < length) {
            rails[i][k++] = cipher[j++];
            cycle = cycleLength(i, k, n, cycle);
            counter += cycle;
        }
        rails[i][k] = '\0';
    }

    for (i = j = 0; i < length; i++) {
        message[i] = popFirst(rails[j]);
        if (forward) {
            j++;
            if (j == n - 1)
                forward = false;

        }
        else {
            j--;
            if (j == 0)
                forward = true;
        }
    }
    message[i] = '\0';
    freeRails(rails, n);
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

    rails = rand() % (length / 3 + 1 - 2) + 2;
    cipher = railFenceCipher(message, length, rails);
    printf("Encrypted message: %ls\n", cipher);
    free(message);
    message = railFenceDecipher(cipher, length, rails);
    printf("Decrypted message: %ls\n", message);
    free(message);
    free(cipher);
    return 0;
}
