def somar_pares(inicio, fim):
    soma = 0
    contador = inicio

    while contador <= fim:
        if contador % 2 == 0:
            soma += contador

        contador += 1

    return soma


inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

resultado = somar_pares(inicio, fim)

print("A soma dos números pares é:", resultado)