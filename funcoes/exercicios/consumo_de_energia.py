def calcular_conta():
    consumo = float(input("Digite o consumo em kWh: "))
    preco_kwh = float(input("Digite o preço do kWh: R$ "))

    valor_conta = consumo * preco_kwh

    print(f"Valor da conta: R$ {valor_conta:.2f}")


def calcular_conta()