def remover_item(itens, posicao):
    elemento = itens.pop(posicao)
    return elemento


itens = ["Caderno", "Caneta", "Lápis", "Borracha"]

print("Itens:", itens)

posicao = int(input("Digite a posição do item que deseja remover: "))

if 0 <= posicao < len(itens):
    removido = remover_item(itens, posicao)

    print("Elemento removido:", removido)
    print("Lista atualizada:", itens)
else:
    print("Posição inválida.")