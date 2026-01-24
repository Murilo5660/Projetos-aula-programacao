senha = "1234"
usuario = "Murilo"

usuario_digitado = input("Digite seu nome de usuário: ")
senha_digitada = input("Digite a senha: ")

while usuario_digitado != usuario or senha_digitada != senha:
    print("Acesso negado! Tente novamente...")
    usuario_digitado = input("Digite seu nome de usuário: ")
    senha_digitada = input("Digite a senha: ")

print(f"Acesso concedido! Seja bem-vindo, usuário {usuario}!")
