notas = 0
soma = 0

for i in range(3):
    notas = float(input("Digite suas notas: "))
    soma += notas

med = soma / 3

if med >= 7.0:
    print("Aprovado.")
elif med >= 5.0 and med < 7.0:
    print("Recuperação.")
else:
    print("Reprovado.")
