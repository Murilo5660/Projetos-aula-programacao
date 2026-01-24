temperatura = float(input('Digite a temperatura em Celsius (Ex.: 23.7): '))
if temperatura < 15:
    print("Temperatura Baixa - Ligar Aquecedor")
elif temperatura >= 15 and temperatura >= 30:
    print("Temperatura Ideal - Sistema em Espera")
elif temperatura > 30:
    print("Temperatura Alta - Ligar Exaustores")
else:
    print('Temperatura não aceita.')
