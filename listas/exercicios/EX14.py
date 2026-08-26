def adicionar_produtos(compras, produtos):
    compras.extend(produtos)


def cancelar_compra(compras, produto):
    if produto in compras:
        compras.remove(produto)
        print("Produto removido da compra.")
    else:
        print("Produto não encontrado na lista.")


compras = ["Arroz", "Feijão", "Leite"]

produtos = ["Pão", "Café", "Açúcar"]

adicionar_produtos(compras, produtos)

print("Lista de compras:", compras)

produto = input("Digite o produto que deseja cancelar: ")

cancelar_compra(compras, produto)

print("Lista atualizada:", compras)