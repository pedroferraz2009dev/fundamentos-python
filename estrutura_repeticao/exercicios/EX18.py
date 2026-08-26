def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = valor // nota

        if quantidade > 0:
            print("Notas de R$", nota, ":", quantidade)

        valor = valor % nota

    if valor != 0:
        print("Não é possível representar o valor restante de R$", valor)


valor = int(input("Digite o valor do saque: "))

caixa_eletronico(valor)