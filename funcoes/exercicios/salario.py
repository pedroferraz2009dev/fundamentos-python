def calcular_salario():
    valor_hora = float(input("Digite o valor da hora trabalhada: R$ "))
    horas = float(input("Digite a quantidade de horas trabalhadas: "))

    salario = valor_hora * horas

    print(f"Salário: R$ {salario:.2f}")


calcular_salario()