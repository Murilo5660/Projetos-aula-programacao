matriz = [
 [14 , 42 , 32] ,
 [41 , 56 , 54] ,
 [20 , 78 , 65]
 ]

soma_diagonal = 0

for i in range(3):
    print(matriz[i])
    soma_diagonal += matriz [i][i]

print(f"A soma da diagonal principal é: {soma_diagonal}")
