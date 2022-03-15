def invert(string):
    for c in range(len(string) - 1, -1, -1):
        print(string[c], end='')
    print("")


print("Este programa recebe uma sequência de texto e a devolve invertida.")

invert(input("Digite um texto a ser invertido: "))
