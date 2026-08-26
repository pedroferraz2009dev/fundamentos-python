def mostrar_impares(numero):
    contador = 1

    while contador <= numero:
        if contador % 2 != 0:
            print(contador)

        contador += 1


numero = int(input("Digite um número inteiro: "))

mostrar_impares(numero)