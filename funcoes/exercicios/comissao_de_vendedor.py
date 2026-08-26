def calcular_salario():
    salario_fixo = float(input("Digite o salário fixo: R$ "))
    vendas = float(input("Digite o valor das vendas: R$ "))
    percentual = float(input("Digite o percentual de comissão: "))

    comissao = vendas * percentual / 100
    salario_final = salario_fixo + comissao

    print(f"Salário final: R$ {salario_final:.2f}")


def calcular_salario()