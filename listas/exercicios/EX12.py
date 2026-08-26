def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)

    return total / quantidade


notas = [7.5, 8.0, 6.5, 9.0]

media = calcular_media(notas)

print("Notas:", notas)
print("Média:", media)