def toSeconds (hours, minutes, seconds):
    return float(hours) * 360 + float(minutes) * 60 + float(seconds)

print("Este programa converte uma quantidade de horas, minutos e segundos em um total de segundos apenas")
print("Total em segundos:", toSeconds(
input("Digite um número de horas: "),
input("Digite um número de minutos: "),
input("Digite um número de segundos: ")))
