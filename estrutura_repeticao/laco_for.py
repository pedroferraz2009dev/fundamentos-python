# Laço for simples
import time


def mostrar_numero():
    for i in range(1, 6):
        print(f'O numero atual é {i}')
        time.sleep(5)

#mostrar_numero()

def mostrar_numero_alternado():
    for num in range(0, 20, 2):
        print(f'O numero atual é {num}')

#mostrar_numero_alternado()


def somar_numeros():
    total = 0
    for valor in range(1, 20):
        total += valor

    print(total)

somar_numeros()