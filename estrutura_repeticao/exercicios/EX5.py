def tabuada(numero):
    contador = 1

    while contador <= 10:
        resultado = numero * contador
        print(numero, "x", contador, "=", resultado)
        contador += 1


numero = int(input("Digite um número: "))

tabuada(numero)