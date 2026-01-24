print("\n--- Tabuada ---")
numero = int(input("Digite um número para ver a tabuada: "))
with open("tabuada.txt","w") as arquivo:
    for i in range(1, 11):
        resultado = numero * i
        linha = f"{numero} x {i} = {resultado}\n"
        arquivo.write(linha)
print(f"A tabuada do número {numero} foi salva no arquivo 'tabuada.txt'")
