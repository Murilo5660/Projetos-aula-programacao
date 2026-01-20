nome_produto = []
preco_produto = []

while True:
    opcoes = input("Digite a opção desejada: \n1) Adicionar um produto e o preço dele. \n2) Listar os produtos. \n3) Calcular todos os preços. \nCaso deseja parar o programa digite 0. \n")
    if opcoes == "1":
        nome = input("Digite o nome do produto que deseja adiconar: ")
        preco = float(input("Digite o preço do produto: "))
        nome_produto.append(nome)
        preco_produto.append(preco)

    elif opcoes == "2": 
        print(f"Produtos das listas: {nome_produto} preço: {preco_produto}")
    
    elif opcoes == "3":
        soma = sum(preco_produto)
        print(f"A soma dos produtos é: R$ {soma}")
    elif opcoes == "0":
        break
    else:
        print("Opção inválida, tente novamente.")
