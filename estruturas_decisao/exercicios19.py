def classificar_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    print("Número:", numero)
    print("Classificação:", sinal, "e", paridade)


classificar_numero()