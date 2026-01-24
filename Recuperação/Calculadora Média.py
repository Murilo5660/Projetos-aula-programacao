notas = []
while True:
    print('\n||| MENU |||')
    print('1-Incerir nova nota')
    print('2-Ver notas lançadas')
    print('3-Calcular mádia final')
    print('0-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        nota = float(input('Digite a nova nota: '))
        notas.append(nota)
        print('Noata adicionada com sucesso!')
    
    elif op == 2:
        if len(notas) == 0:
            print('Nenhuma nota foi lançada ainda.')
        else:
            print(f'Notas lançadas: {notas}')
    
    elif op == 3:
        if len(notas) == 0:
            print('não há notas para calcular a média.')
        else:
            med = sum(notas) / len(notas)
            print(f'Média final: {med:.2f}')
    
    elif op == 0:
        print('Programa encerrado.')
        break
    
    else:
        print('Opção inválida! Digite uma opção exitente(Ex.:1,2,3,0).')
