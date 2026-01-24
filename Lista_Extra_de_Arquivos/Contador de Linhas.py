nome = input("Digite o nome de um arquivo para contar as linhas |ex: perfil.txt|: ")
with open(nome,"r") as arquivo:
    linhas = arquivo.readlines()
quantidade = len(linhas)
print(f"O arquivo '{nome}' tem {quantidade} linhas")

# Exercício 6 - Copiador de Arquivos
print("\n--- Copiador de Arquivos ---")
original = input("Digite o nome do arquivo que será copiado |ex: tarefa.txt|: ")
copia = input("Digite o nome do novo arquivo |ex: copia.txt|: ")
with open(original,"r") as orig:
    conteudo = orig.read()
with open(copia,"w") as copi:
    copi.write(conteudo)
print(f"Arquivo '{original}' copiado com sucesso para '{copia}'!")
