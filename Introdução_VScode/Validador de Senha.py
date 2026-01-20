senha_correta = 5660
senha = int(input("Digite sua senha: "))

while senha:
    if senha == senha_correta:
        break
    else: 
        senha = int(input("Senha incorreta. Tente novamente: "))
print("Acesso Concedido.")
