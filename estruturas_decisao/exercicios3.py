def verificar_idade():
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Menor de idade")
    elif idade >= 18:
        print("Maior de idade")
    else:
        print("Idade inválida")


verificar_idade()