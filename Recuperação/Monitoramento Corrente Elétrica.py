correntes = [0.5 , 1.2 , 0.8 , 1.5 , 0.6 , 1.1 , 0.9 , 1.3]
soma = 0
leituras = 0

for i in correntes:
    soma += i
    if i >= 1.0:
        leituras += 1
    
media = soma / len(correntes)

print(f"A média das correntes medidas é: {media}")
print(f"As leituras maiores que 1.0 são: {leituras}")
