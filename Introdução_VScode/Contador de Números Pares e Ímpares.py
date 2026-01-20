pares = 0
impares = 0

for i in range(10):
    num = int(input("Digite números: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: \n {pares} \n Números impares: \n {impares}")
