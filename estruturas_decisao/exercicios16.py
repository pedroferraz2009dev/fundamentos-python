def sistema_login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso")
    elif usuario == "admin" and senha != "1234":
        print("Senha incorreta")
    else:
        print("Usuário não encontrado")


sistema_login()