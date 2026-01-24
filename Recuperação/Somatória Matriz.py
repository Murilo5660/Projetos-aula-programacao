matriz = []
print('\n\nDigite os valores da matriz 3x3: ')
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

print('\nMatriz digitada:')
for linha in matriz:
    print(linha)

diagonais = 0
for i in range(3):
    diagonais += matriz[i][i]

print(f'Soma da diagonal principal: {diagonais}')
