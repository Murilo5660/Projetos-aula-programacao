nivel = float(input('Qual o nível de água do reservatório (%): '))

if nivel < 20:
    print("Nível Crítico - Ligar Bomba de Emergência")
elif 20 >= nivel <= 80:
    print("Nível Operacional - Monitorar")
elif nivel > 80 and nivel <= 100:
    print("Nível Alto - Desligar Entrada")
else:
    print('Nível de água não aceito, digite novamente!')
