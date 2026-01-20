with open ("tarefas.txt", "a") as tarefas:
    tarefa_desejada = input("Digite sua tarefa: ")
    tarefas.write(tarefa_desejada + "\n")

with open ("tarefas.txt", "r") as tarefas:
    conteudo = tarefas.read()

print(conteudo)
