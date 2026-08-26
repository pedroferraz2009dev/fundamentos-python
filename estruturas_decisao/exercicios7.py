def classificar_temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))

    if temperatura < 15:
        print("Frio")
    elif temperatura <= 25:
        print("Agradável")
    else:
        print("Quente")


classificar_temperatura()