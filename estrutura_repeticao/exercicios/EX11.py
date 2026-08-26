def fatorial(numero):
    resultado = 1
    contador = 1

    while contador <= numero:
        resultado *= contador
        contador += 1

    return resultado


numero = int(input("Digite um número inteiro: "))

resultado = fatorial(numero)

print("O fatorial de", numero, "é:", resultado)