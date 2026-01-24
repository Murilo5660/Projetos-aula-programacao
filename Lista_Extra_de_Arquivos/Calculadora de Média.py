print("\n--- Calculadora de Média ---")
with open("notas.txt","w") as arquivo:
    arquivo.write("8.5\n")
    arquivo.write("9.0\n")
    arquivo.write("7.5\n")
    arquivo.write("10.0\n")
    arquivo.write("6.0\n")

with open("notas.txt","r") as arquivo:
    linhas = arquivo.readlines()
notas = [float(linha.strip()) for linha in linhas]
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")
