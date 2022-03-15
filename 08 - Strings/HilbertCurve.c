#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * axiom () {
    char *str = malloc(2 * sizeof(char));
    str[0] = 'A';
    str[1] = '\0';
    return str;
}

char * initializeNewString (char * prevStr) {
    int i, size;
    char *newStr;

    size = i = 0;
    do {
        if (prevStr[i] == 'A' || prevStr[i] == 'B')
            size += 11;
        else
            size++;
    } while (prevStr[i++] != '\0');
    newStr = malloc(size * sizeof(char));
    newStr[0] = '\0';
    return newStr;
}

char * transformString(char *prevStr) {
    int i;
    char *newStr = initializeNewString(prevStr);

    for (i = 0; prevStr[i] != '\0'; i++)
        if (prevStr[i] == 'A')
            strcat(newStr, "+BF-AFA-FB+");
        else if (prevStr[i] == 'B')
            strcat(newStr, "-AF+BFB+FA-");
        else
            strncat(newStr, prevStr + i, 1);
    free(prevStr);
    return newStr;
}

char * HilbertCurve (char *str, int n) {
    if (n == 0)
        return str;
    return HilbertCurve(transformString(str), --n);
}

void printInstructions (char *str) {
    if (*str == '\0')
        printf("\n");
    else if ((str[0] == '+' && str[1] == '-') || (str[0] == '-' && str[1] == '+'))
        printInstructions(str + 2);
    else {
        printf("%c", *str);
        printInstructions(str + 1);
    }
}

int main () {
    int n;
    char *str;

    printf("This program produces instructions for drawing a Hilbert's curve of complexity n, n ∈ ℕ.\nType in a value for n and press ENTER: ");
    if (scanf(" %d", &n) == EOF || n < 0) {
        printf("Error: n is not a natural number.\n");
        return 1;
    }

    str = HilbertCurve(axiom(), n);
    printf("Drawing instructions:\n");
    printInstructions(str);
    free(str);
    return 0;
}
