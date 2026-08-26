def contar_pares(inicio, fim):
    quantidade = 0
    contador = inicio

    while contador <= fim:
        if contador % 2 == 0:
            quantidade += 1

        contador += 1

    return quantidade


inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

resultado = contar_pares(inicio, fim)

print("Quantidade de números pares:", resultado)