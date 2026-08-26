def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas


temperaturas = [25, 30, 22, 28, 20, 32]

quantidade, soma, media, ordenadas = analisar_temperaturas(temperaturas)

print("Temperaturas:", temperaturas)
print("Quantidade:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Temperaturas ordenadas:", ordenadas)