# Exercício 4: Criar lista de tarefas
with open("tarefas.txt", "w") as arquivo_tarefas:
    print("Por favor, digite 3 tarefas a serem feitas:")
    for i in range(3):
        tarefa = input(f"Tarefa {i+1}: ")
        arquivo_tarefas.write(tarefa + "\n")

print("\nLista de tarefas foi salva em 'tarefas.txt'!")


# Exercício 5: Ler lista de tarefas
print(" --- Minha Lista de Tarefas ---")
try:
    with open("tarefas.txt", "r") as arquivo_tarefas:
        numero_tarefa = 1
        for tarefa in arquivo_tarefas:
            print(f"{numero_tarefa}. {tarefa.strip()}")
            numero_tarefa += 1
except FileNotFoundError:
    print("Arquivo 'tarefas.txt' não encontrado. Rode o exercício 4 primeiro.")
