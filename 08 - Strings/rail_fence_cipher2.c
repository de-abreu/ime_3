#include <stdlib.h>
#include <locale.h>
#include <wchar.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct node {
    wchar_t ch;
    struct node *next;
} Node;

typedef struct {
    Node *start;
    Node *end;
} Rail;

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

Rail * initializeRail () {
    Rail * r = malloc(sizeof(Rail));
    r->start = NULL;
    return r;
}

Node * createNode (wchar_t c) {
    Node *n = malloc(sizeof(Node));
    n->ch = c;
    return n;
}

void addNode (Rail *r, wchar_t c) {
    Node *n = createNode(c);

    if (r->start)
        r->end->next = n;
    else
        r->start = r->end = n;
    r->end = n;
}

Rail ** loadRails(wchar_t *cipher, int length, int n) {
    int i, j, counter, cycle;
    Rail **rails = malloc(n * sizeof(Rail*));

    for (i = j = 0; i < n; i++) {
        counter = i;
        rails[i] = initializeRail();
        while (counter < length) {
            addNode(rails[i], cipher[j++]);
            cycle = cycleLength(i, counter, n, cycle);
            counter += cycle;
        }
    }
    return rails;
}

wchar_t popFirst (Rail *r) {
    Node *n = r->start;
    wchar_t c = n->ch;
    if (n != r->end)
        r->start = n->next;
    else
        free(r);
    free(n);
    return c;
}

wchar_t * unloadRails (Rail ** rails, int length, int n) {
    wchar_t *message = malloc(length * sizeof(wchar_t));
    int i, j;
    bool forward = true;

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
    free(rails);
    return message;
}

wchar_t * railFenceDecipher(wchar_t *cipher, int length, int n) {
    return unloadRails(loadRails(cipher, length, n), length, n);
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

    rails = randRange(2, length / 3);
    cipher = railFenceCipher(message, length, rails);
    printf("Encrypted message: %ls\n", cipher);
    free(message);
    message = railFenceDecipher(cipher, length, rails);
    printf("Decrypted message: %ls\n", message);
    free(message);
    free(cipher);
    return 0;
}
