#include <stdio.h>
#include <stdbool.h>

bool isBinary (int n) {
    if (n < 0)
        return false;
    while (n > 0) {
        if (n % 10 > 1)
            return false;
        n /= 10;
    }
    return true;
}

int base10 (int binary) {
    if (binary < 10)
        return binary;
    return base10(binary / 10) * 2 + binary % 10;
}

int main() {
    int i;

    printf("This program converts a number from base 2 to base 10.\nType a binary number and press ENTER: ");
    if (!scanf(" %d", &i) || !isBinary(i)) {
        printf("Invalid value passed.\n");
        return 1;
    }
    printf("The binary %d is equivalent to the decimal %d in base 10.\n", i, base10(i));
}
