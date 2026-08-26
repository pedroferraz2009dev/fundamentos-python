def trocar_valores():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    print("\nAntes:")
    print("A =", a)
    print("B =", b)

    a, b = b, a

    print("\nDepois:")
    print("A =", a)
    print("B =", b)


def car_valores()