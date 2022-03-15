def countDigits(n):
    digits = 1

    if (n < 0):
        n = -n
    while n // 10 != 0:
        digits += 1
        n //= 10
    return digits


print("Este programa aceita um valor inteiro n e contabiliza seu número de dígitos.")

try:
    n = int(input("Digite um valor inteiro para n: "))
except ValueError:
    print("Erro: não é um valor inteiro.")
    exit()
except EOFError:
    print("")
    exit()
print("O número", n, "tem", countDigits(n), "dígitos.")
