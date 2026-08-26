def calcular_imc():
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))

    imc = peso / (altura ** 2)

    print(f"IMC: {imc:.2f}")


def calcular_imc()