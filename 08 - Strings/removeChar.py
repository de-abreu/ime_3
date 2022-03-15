def removeChar(string, char):
    print("\nTexto sem o caractere \"" + char[0], end="\": ")
    for c in string:
        if c != char[0]:
            print(c, end='')
    print("")


print("Este programa recebe uma sequência de texto e remove desta um dado tipo de caractere.")

removeChar(
    input("\nDigite uma sequência de texto: "),
    input("\nDigite um tipo de caractere a ser removido desta: ")
)
