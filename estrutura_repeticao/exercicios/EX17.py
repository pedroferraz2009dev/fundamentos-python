def jogo_adivinhacao(numero_secreto):
    while True:
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite > numero_secreto:
            print("O palpite é maior que o número secreto.")
        else:
            print("O palpite é menor que o número secreto.")


jogo_adivinhacao(7)