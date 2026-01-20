with open("diario.txt", "r") as arquivo:
    conteudo = arquivo.read()

with open("copia_diario.txt", "w") as copia_diario:
    copia_diario.write(conteudo)
