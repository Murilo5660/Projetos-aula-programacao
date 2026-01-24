print("\n--- Agenda de Contatos ---")
with open("agenda.csv","w") as arquivo:
    arquivo.write("Caio,12345-6789\n")
    arquivo.write("André,98765-4321\n")
    arquivo.write("Márcio,24682-4286\n")
    arquivo.write("Henrique,13579-7531\n")
    arquivo.write("Fernando,01000-1101\n")

print("1 = Adicionar contato")
print("2 = Listar contatos")
print("3 = Buscar contato")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    with open("agenda.csv","a") as arquivo:
        arquivo.write(f"{nome},{telefone}\n")
    print(f"Contato '{nome}' adicionado com sucesso!")

elif opcao == "2":
    with open("agenda.csv","r") as arquivo:
        linhas = arquivo.readlines()
    print("\nContatos cadastrados:")
    for linha in linhas:
        nome, telefone = linha.strip().split(",")
        print(f" - {nome} | {telefone}")

elif opcao == "3":
    busca = input("Digite o nome do contato para buscar: ").lower()
    with open("agenda.csv","r") as arquivo:
        linhas = arquivo.readlines()

    contador = 0
    for linha in linhas:
        nome, telefone = linha.strip().split(",")
        if busca in nome.lower():
            print(f" - {nome} | {telefone}")
            contador += 1
        
    if contador == 0:
        print(f"Nenhum contato com o nome '{busca}' encontrado.")

else:
    print("Opção inválida! Escolha |1, 2 ou 3|")
