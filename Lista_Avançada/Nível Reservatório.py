nivel = float(input("Digite o nível do seu reservatório: "))

if nivel < 20:
    print("Nível Crítico - Ligar Bomba de Emergência")

elif nivel >= 20 and nivel <= 80:
    print("Nível Operacional - Monitorar")

elif nivel > 80 and nivel <= 100:
    print("Nível Alto - Desligar Entrada")

else:
    print("Porcentagem inválida")
