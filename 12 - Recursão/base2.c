#include <stdio.h>

int base2 (int i) {
    if (i < 2)
        return i;
    return base2(i / 2) * 10 + (i % 2);
}

int main() {
    int i;

    printf("This program converts a number from base 10 to base 2.\nType a non-negative integer value: and press ENTER: ");
    if (!scanf(" %d", &i) || i < 0) {
        printf("Invalid value passed.\n");
        return 1;
    }
    printf("The decimal %d is equivalent to the binary %d in base 2.\n", i, base2(i));
}
