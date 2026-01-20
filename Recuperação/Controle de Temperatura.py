temperatura_atual = float(input("Digite a temperatura em °C: "))

if temperatura_atual < 15:
    print("Temperatura Baixa - Ligar Aquecedor")

elif temperatura_atual >= 15 and temperatura_atual <= 30:
    print("Temperatura Ideal - Sistema em Espera")

elif temperatura_atual > 30:
    print("Temperatura Alta - Ligar Exaustores")
