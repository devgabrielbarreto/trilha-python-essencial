usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso liberado ao sistema!")
else:
    print("Usuário ou senha incorretos.")