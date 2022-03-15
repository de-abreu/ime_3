import sys


def average(a, b):
    return (a + b) / 2


def absoluteValue(n):
    return -n if n < 0 else n


def displayRoot(n, epsilon):
    root = n
    i = delta = 0

    if n != 0 and n != 1:
        if n > 1:
            suplim = n
            inflim = 1
        else:
            suplim = 1
            inflim = n

        while True:
            i += 1
            root = average(suplim, inflim)
            delta = absoluteValue(root**2 - n)
            if root**2 > n:
                suplim = root
            else:
                inflim = root
            if delta <= epsilon:
                break

    print("\nNúmero de iterações:", i)
    print("Diferença absoluta:", delta)
    print("Raiz quadrada:", root)


print("Este programa calcula a raiz quadrada de n com uma margem de erro menor que epsilon, sendo ambos números não negativos e o último não nulo.")

try:
    n, epsilon = input(
        "Digite, separados por espaço, valores para n e epsilon: ").split()
    n = float(n)
    epsilon = float(epsilon)
except ValueError:
    print("Erro: valor inválido detectado.")
    sys.exit()
except EOFError:
    print("")
    sys.exit()
if n < 1 or epsilon < 0:
    print("Erro: valor inválido detectado.")
    sys.exit()

displayRoot(n, epsilon)
