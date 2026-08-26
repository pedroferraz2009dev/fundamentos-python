def eh_primo(numero):
    if numero < 2:
        return False

    contador = 2

    while contador < numero:
        if numero % contador == 0:
            return False

        contador += 1

    return True


numero = int(input("Digite um número inteiro: "))

resultado = eh_primo(numero)

print("É primo?", resultado)