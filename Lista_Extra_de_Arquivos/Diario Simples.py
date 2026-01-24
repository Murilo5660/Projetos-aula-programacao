# Exercício 1: Criar arquivo e escrever
with open("Meu_Diário.txt", "w") as bloco:
    bloco.write("Hoje, 3 de outubro de 2025, elaborei uma atividade em código sobre arquivo.txt.\n")

print("Arquivo 'Meu_Diário.txt' criado com sucesso!")


# Exercício 2: Ler o conteúdo do arquivo
try:
    with open("Meu_Diário.txt", "r") as bloco:
        conteudo = bloco.read()
        print(" --- Conteúdo do Diário ---")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo 'Meu_Diário.txt' ainda não existe. Rode o exercício 1 primeiro.")


# Exercício 3: Acrescentar informação ao arquivo
with open("Meu_Diário.txt", "a") as bloco:
    bloco.write("Estou aprendendo a manipular arquivos e é muito útil.\n")

print("Nova anotação no Meu Diário!")

sentimento = input("Como você está se sentindo hoje? ")
with open("Meu_Dário.txt","a") as arquivo:
    arquivo.write(sentimento + "\n")
print("Anotação salva!")

