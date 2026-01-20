lista_A = [1,2,3,4,5]
lista_B = [4,5,6,7,8]
comuns = []
for itenA in lista_A:
    if itenA in lista_B:
        comuns.append(itenA)

print(comuns)
