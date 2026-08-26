def mostrar_primos(inicio, fim):
    numero = inicio

    while numero <= fim:
        if numero >= 2:
            contador = 2
            primo = True

            while contador < numero:
                if numero % contador == 0:
                    primo = False
                    break

                contador += 1

            if primo:
                print(numero)

        numero += 1


inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

mostrar_primos(inicio, fim)