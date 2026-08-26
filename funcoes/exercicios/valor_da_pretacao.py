def calcular_prestacao():
    valor = float(input("Digite o valor do produto: R$ "))
    parcelas = int(input("Digite a quantidade de parcelas: "))

    valor_parcela = valor / parcelas

    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")


def calcular_prestacao()