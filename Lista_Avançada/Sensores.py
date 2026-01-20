tensoes = [12.5 , 11.9 , 13.1 , 10.5 , 12.0 , 11.8 , 13.5 , 12.2 , 11.5 , 12.8]
soma = 0
fora_faixa = 0

for i in tensoes:
    soma += i
    if i < 11.5 or i > 12.5:
        fora_faixa += 1

media = soma / len(tensoes)
max(tensoes)
min(tensoes)

print(f"A média é: {media}")
print(f"A maior tensão registrada é: {max(tensoes)} e a menor é: {min(tensoes)}")
print(f"Leituras fora da faixa: {fora_faixa}")
