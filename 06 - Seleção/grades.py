import sys

def grade(points):
    if points >= 90:
        return "A"
    elif points >= 80:
        return "B"
    elif points >= 70:
        return "C"
    elif points >= 60:
        return "D"
    return "F"

print("Este programa dá uma nota de A a F para uma quantia de pontos 0 até 100 pontos")
try:
    points = float(input("Digite um valor para epsilon: "))
except ValueError:
    print("Erro: não é um número real.")
    sys.exit()
except EOFError:
    print("")
    sys.exit()
if points < 0 or points > 100:
    print("Erro: valor inválido.")
    sys.exit()
print("A nota para um total de", points, "pontos é", grade(points))
