print("Agenda de contatos, opções: \n1) Adicionar um novo contato(nome e telefone, exemplo: \nNome: Murilo \nTelefone: 98764-3210\n2) Listar todos os contatos salvos.\n3) Buscar um contato atrasvés do nome.")
opcoes = input("Escolha uma das opções que deseja: ")

if opcoes == "1" or opcoes == "Adicionar contato" or opcoes == "adicionar contato" or opcoes == "add contato":
    nome = input("Digite o nome do contato desejado: ")
    telefone = input("Digite o telefone do contato desejado: ")
    
    with open("agenda.csv", "a") as arquivo:
         arquivo.write(f"{nome}, {telefone}\n")
    print(f"O Contato '{nome}' foi adicionado com sucesso!")
elif opcoes == "2" or opcoes == "Listar contatos salvos" or opcoes == "listar contatos salvos" or opcoes == "Listar contatos" or opcoes == "listar contatos":
     try:
          with open("agenda.csv", "r") as arquivo:
               conteudo_salvo = arquivo.readlines()
               if len(conteudo_salvo) == 0:
                 print("A agenda está vazia.")
               else:
                    print("\nContatos Salvos / cadastrados: ")
                    for linha in conteudo_salvo:
                         conteudo_completo = linha.strip()
                         print(conteudo_completo)
     except FileNotFoundError:
          print("Nenhum contato encontrado.")
elif opcoes == "3" or opcoes == "Buscar um contato" or opcoes == "buscar um contato" or opcoes == "Buscar contato" or opcoes == "buscar contato":
     nome_p_buscar = input("Digite o nome que desejado: ")
     with open("agenda.csv","r") as arquivo:
          conteudo_salvo = arquivo.read()
          print(f"O contato {nome_p_buscar} é: {nome_p_buscar in conteudo_salvo}")
else: 
     print("Opção inválida, tente novamente.")
