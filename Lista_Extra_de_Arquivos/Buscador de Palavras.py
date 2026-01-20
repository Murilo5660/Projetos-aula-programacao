palavra = input("Me diga uma palavra que você quer encontrar: ").lower()
nome_arquivo = input("Qual o nome do arquivo? ")

try:
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read().lower()
    arquivo.close()

    palavras = texto.split()
    quantidade = palavras.count(palavra)

    print(f"A palavra {palavra} aparece {quantidade} vezes no arquivo {nome_arquivo}.")
except FileNotFoundError:
    print("Não consegui encontrar esse arquivo. Você digitou corretamente ?")
