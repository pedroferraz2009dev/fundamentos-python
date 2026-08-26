def mostrar_multiplos(numero):
    contador = 1

    while contador <= 10:
        print(numero * contador)
        contador += 1


numero = int(input("Digite um número inteiro: "))

mostrar_multiplos(numero)