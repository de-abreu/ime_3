import sys


def pi(n):
    pi = 0

    for i in range(n):
        step = 4 / (2 * i + 1)
        pi += step if i % 2 == 0 else -step
    return pi


print("Este programa calcula o valor aproximado de π fazendo uso da fórmula de Leibniz. O grau de precisão do resultado é dado pelo valor de epsilon, um número inteiro e não negativo.")

try:
    epsilon = int(input("Digite um valor para epsilon e pressione ENTER: "))
except ValueError:
    print("Erro: não é um valor inteiro.")
    sys.exit()
except EOFError:
    print("")
    sys.exit()
if epsilon < 0:
    print("Erro: valor negativo.")
    sys.exit()
print("O valor aproximado de π para epsilon =", epsilon, "é", pi(epsilon))
