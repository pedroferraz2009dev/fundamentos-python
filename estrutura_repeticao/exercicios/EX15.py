def maior_numero():
    maior = None

    while True:
        numero = float(input("Digite um número: "))

        if maior is None or numero > maior:
            maior = numero

        continuar = input("Deseja continuar? (s/n): ").lower()

        if continuar == "n":
            break

    return maior


resultado = maior_numero()

print("O maior número informado foi:", resultado)