#include <stdio.h>
#include <stdlib.h>

typedef struct instruction{
    char instruction;
    struct instruction *next;
} Instruction;

Instruction * newInstruction (char instruction) {
    Instruction *i = malloc(sizeof(Instruction));
    i->instruction = instruction;
    return i;
}

Instruction * axiom () {
    Instruction *HEAD = newInstruction('\0');

    HEAD->next = newInstruction('A');
    HEAD->next->next = NULL;
    return HEAD;
}

void freeList (Instruction *list) {
    Instruction *prev;

    if (!list)
        return;
    prev = list;
    list = list->next;
    free(prev);
    freeList(list);
}

char * char2str (char c) {
    char * str = malloc(2 * sizeof(char));
    str[0] = c;
    str[1] = '\0';
    return str;
}

Instruction * addInstructions (Instruction *j, char *instructions) {
    int i;

    for (i = 0; instructions[i] != '\0'; i++) {
        j->next = newInstruction(instructions[i]);
        j = j->next;
    }
    return j;
}

Instruction * transformInstruction (Instruction *list) {
    Instruction *i = list->next, *j = newInstruction('\0'), *newList = j;
    char *str;

    while (i) {
        if (i->instruction == 'A')
            j = addInstructions(j, "+BF-AFA-FB+");
        else if (i->instruction == 'B')
            j = addInstructions(j, "-AF+BFB+FA-");
        else{
            str = char2str(i->instruction);
            j = addInstructions(j,str);
            free(str);
        }
        i = i->next;
    }

    j->next = NULL;
    freeList(list);
    return newList;
}

Instruction * HilbertCurve (Instruction *list, int n) {
    if (n == 0)
        return list;
    return HilbertCurve(transformInstruction(list), --n);
}

void simplifyInstructions (Instruction *i) {
    Instruction * next;

    if (!i->next || !i->next->next)
        return;
    if ((i->next->instruction == '+' && i->next->next->instruction == '-')
    || (i->next->instruction == '-' && i->next->next->instruction == '+')) {
        next = i->next->next->next;
        i->next->next = NULL;
        freeList(i->next);
        i->next = next;
        simplifyInstructions(i);
    }
    else
        simplifyInstructions(i->next);
}

void printInstructions(Instruction *list) {
    while (list->next) {
        printf("%c", list->next->instruction);
        list = list->next;
    }
    printf("\n");
}

int main () {
    int n;
    Instruction *HEAD;

    printf("This program produces instructions for drawing a Hilbert's curve of complexity n, n ∈ ℕ.\nType in a value for n and press ENTER: ");
    if (scanf(" %d", &n) == EOF || n < 0) {
        printf("Error: n is not a natural number.\n");
        return 1;
    }

    HEAD = HilbertCurve(axiom(), n);
    simplifyInstructions(HEAD);
    printf("Drawing instructions:\n");
    printInstructions(HEAD);
    freeList(HEAD);
    return 0;
}
