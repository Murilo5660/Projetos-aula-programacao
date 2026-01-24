print("1 = Adicionar uma tarefa")
print("2 = Listar todas as tarefas")
opcao = input("Escolha uma opção |1 ou 2|: ")

if opcao == "1":
    tarefa = input("Digite a tarefa: ")
    with open("tarefa.txt","a") as arquivo:
        arquivo.write(tarefa + "\n")
    print("Tarefa adicionada!")

elif opcao == "2":
    with open("tarefa.txt","r") as arquivo:
        tarefas = arquivo.readlines()
    print("\nSuas tarefas:")
    for tarefa in tarefas:
        print("-", tarefa.strip())

else:
    print("Opção inválida! Escolha |1 ou 2|")
