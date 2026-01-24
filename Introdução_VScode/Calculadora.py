#Calculadora do Murilo

# Entrada de dados: pedir ao usuário 2 números
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Dgite o segundo número: '))

# Menu de operações
print('\nQual operação deseja realizar?')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potenciação')

op = input("Escolha a operção (1-5): ")

# Processamento das operações
print('\n--- Resultado ---')

# Soma
if op == "1":
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')

#Subtração
elif op == "2":
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')

#Multiplicação
elif op == "3":
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado}')

#Divisão com tratamento de erro
elif op == "4":
    if num2 == 0:
        print("Erro: não é possível dividir por zero!")
    else:
        resultado = num1 / num2
        print(f'{num1} / {num2} = {resultado}')

#Potenciação com regra especial: todo número elevado a 0 é 1
elif op == "5":
    if num2 == 0:
        print('Resultado da potenciação:', 1)
    else:
        resultado = num1 ** num2
        print(f'{num1}^{num2} = {resultado}')

else:

    print('Opção inválida! Escolha um número entre 1 e 5.')
