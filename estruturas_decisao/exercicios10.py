def calcular_desconto():
    valor = float(input("Digite o valor da compra: R$ "))

    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.15

    valor_final = valor - desconto

    print("Desconto: R$", desconto)
    print("Valor final: R$", valor_final)


calcular_desconto()