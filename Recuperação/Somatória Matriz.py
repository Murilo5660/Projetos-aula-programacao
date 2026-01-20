matriz = [
 [9 , 8 , 3],
 [1 , 6 , 4],
 [2 , 7 , 5]
]
soma_total = 0

for linha in matriz:
    for elemento in linha:
        soma_total += elemento

print(f"A soma total é: {soma_total}")
