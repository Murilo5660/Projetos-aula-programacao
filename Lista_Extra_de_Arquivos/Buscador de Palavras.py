# Exercício 9 - Buscador de Palavras
print("\n--- Buscador de Palavras ---")
nome_arquivo = input("Digite o nome do arquivo |ex: tarefa.txt|: ")
palavra = input("Digite a palavra que deseja buscar: ")
with open(nome_arquivo,"r") as arquivo:
    conteudo = arquivo.read()
quantidade = conteudo.lower().count(palavra.lower())
print(f"A palavra '{palavra}' aparece {quantidade} vezes no arquivo '{nome_arquivo}'")
