def somar_ate(numero):
    soma = 0
    contador = 1

    while contador <= numero:
        soma += contador
        contador += 1

    return soma


numero = int(input("Digite um número inteiro: "))

resultado = somar_ate(numero)

print("A soma dos números de 1 até", numero, "é:", resultado)