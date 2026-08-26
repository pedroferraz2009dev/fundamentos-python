def login():
        e_mail = "pedroferrazsilva2009@gmail.com"
        senha = "blablabla"
        codigo_secreto = "abcde"

        e_mail_input = input("Digite o e-mail: ")
        senha_input = input("Digite a senha: ")

        if e_mail_input == e_mail and senha_input == senha:
            print("Usuario logado")
            acessar_admin = input("Deseja acessar a area administrativa? [digite S ou N]")
            if acessar_admin == "S":
                codigo_secreto_input = input("Digite o código secreto: ")
                if codigo_secreto_input == codigo_secreto:
                    print("Usuario adm logado")
                else:
                    print("Código errado")
            elif acessar_admin == "N":
                print("OK, voce acessou usuario comum")
            else:
                print("Opção invalida")
        else:
            print("Senha incorreto")

login()