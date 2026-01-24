correntes = [0.5, 1.2, 0.8, 1.5, 0.6, 1.1, 0.9, 1.3]
soma = 0
for valor in correntes:
    soma += valor 

media = soma/len(correntes)
print(f'\nMédia das correntes: {media:.2f} A')

contador = 0 
for valor in correntes:
    if valor > 1.0:
        contador += 1

print(f'Leituras acima de 1.0 A: {contador}')
