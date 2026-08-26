def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Exibir números de 1 a 10")
        print("2. Exibir números pares")
        print("3. Exibir tabuada")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            contador = 1

            while contador <= 10:
                print(contador)
                contador += 1

        elif opcao == 2:
            contador = 2

            while contador <= 10:
                print(contador)
                contador += 2

        elif opcao == 3:
            numero = int(input("Digite um número para a tabuada: "))

            contador = 1

            while contador <= 10:
                print(numero, "x", contador, "=", numero * contador)
                contador += 1

        elif opcao == 4:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


menu()