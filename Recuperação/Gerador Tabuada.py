while True:
    try:
        numero = int(input('\nDigite um número inteiro positivo: '))
        if numero > 0:
            break
        else:
            print('erro: você deve digitar um número positivo!')
    except ValueError :
        print('Erro: você deve digitar um número inteiro!')

print(f'Tabuada do número {numero}:')
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
