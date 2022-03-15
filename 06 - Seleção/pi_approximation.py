def pi(n):
    pi = 0

    for i in range(n):
        pi += (-1)**i * 4 / (2 * i + 1)
    return pi


print("Este programa calcula o valor aproximado de π fazendo uso da fórmula de Leibniz. O grau de precisão do resultado é dado pelo valor de epsilon, um número inteiro e não negativo.")

try:
    epsilon = int(input("Digite um valor para epsilon: "))
except ValueError:
    print("Erro: não é um valor inteiro.")
    exit()
except EOFError:
    print("")
    exit()
if epsilon < 0:
    print("Erro: valor negativo.")
    exit()
print("O valor aproximado de π para epsilon =", epsilon, "é", pi(epsilon))
