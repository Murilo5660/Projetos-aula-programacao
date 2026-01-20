with open("notas.txt", "r") as arquivo:
    notas = []
    for linha in arquivo:
        nota = float(linha.strip())
        notas.append(nota)
med = sum(notas) / len(notas)

print(f'A média das notas é: {med}')
