def contar_ate(numero):
    contador = 1

    while contador <= numero:
        print(contador)
        contador += 1


numero = int(input("Digite um número inteiro: "))

contar_ate(numero)