numero_tabuada = int(input("Digite o tipo de tabuada que desejar do 1 a 10: "))

with open("tabuada.txt", "w") as arquivo:
    for multiplicador in range(1, 11):
        resultado_tabuada = f"{numero_tabuada} x {multiplicador} = {numero_tabuada * multiplicador}\n"
        arquivo.write(resultado_tabuada)
