
while True:
    print('\n=== MENU DO ESTOQUE ===')
    print('1 - Adicionar produto')
    print('2 - Listar produtos')
    print('3 - Valor total do estoque')
    print('0 - Sair')

    op = input('Escolha uma opção: ')

    if op == '1':
        nome = input('Nome do produto: ')
        preco = float(input('Preço do produto: '))
        produtos.append({'nome': nome, 'preco': preco})
        print('Produto adicionado!')

    elif op == '2':
        if not produtos:
            print('\nNenhum produto cadastradoo! Use a opção 1 para adicionar novos produtos.')
        else:
            print('\nProdutos cadastrados:')
            for p in produtos:
                print(f"- {p['nome']} : R$ {p['preco']:.2f}")

    elif op == '3':
        total = sum(p['preco'] for p in produtos)
        print(f'Valor total do estoque: R$ {total:.2f}')

    elif op == '0':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida! Tente novamente.')
