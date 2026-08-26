def verificar_senha():
    senha = input("Digite a senha: ")

    if senha == "python123":
        print("Acesso permitido")
    elif senha != "python123":
        print("Senha inválida")
    else:
        print("Senha inválida")


verificar_senha()