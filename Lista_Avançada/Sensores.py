tensoes = [12.5, 11.9, 13.1, 10.5, 12.0, 11.8, 13.5, 12.2, 11.5, 12.8]

media = sum(tensoes) / len(tensoes)
maior = max(tensoes)
menor = min(tensoes)

faixa_min = 11.5
faixa_max = 12.5
fora_de_faixa = 0

for tensao in tensoes:
    if tensao < faixa_min or tensao > faixa_max:
        fora_de_faixa += 1

print(f'\nMédia das tensões: {media:.2f} V')
print(f'Maior tensão: {maior} V')
print(f'Menor tensão: {menor} V')
print(f'Leituras fora de faixa: {fora_de_faixa}')
