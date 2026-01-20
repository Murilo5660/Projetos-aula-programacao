numero_tabuada = int(input("Digite o tipo de tabuada que desejar do 1 a 10: "))
multiplicador = 0

if numero_tabuada < 0:
        print("Tente novamente.")
else:
    for multiplicador in range(11):
        print(numero_tabuada, " x " , multiplicador, " = ", (numero_tabuada*multiplicador))
