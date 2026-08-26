def verificar_par_impar():
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("O número é par.")
    elif numero % 2 != 0:
        print("O número é ímpar.")
    else:
        print("Valor inválido.")


verificar_par_impar()