def calcular_desconto():
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto: "))

    valor_final = preco - (preco * desconto / 100)

    print(f"Valor final: R$ {valor_final:.2f}")


calcular_desconto()