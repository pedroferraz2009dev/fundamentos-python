def calcular_frete():
    valor = float(input("Digite o valor da compra: R$ "))

    if valor <= 100:
        frete = 20
    elif valor <= 300:
        frete = 10
    else:
        frete = 0

    total = valor + frete

    print("Valor da compra: R$", valor)
    print("Valor do frete: R$", frete)
    print("Valor total: R$", total)


calcular_frete()