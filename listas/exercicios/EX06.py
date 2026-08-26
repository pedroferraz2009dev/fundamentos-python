def encontrar_produto(produtos, produto):
    if produto in produtos:
        return produtos.index(produto)
    else:
        return -1


produtos = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input("Digite o produto que deseja encontrar: ")

posicao = encontrar_produto(produtos, produto)

if posicao != -1:
    print("Produto encontrado na posição:", posicao)
else:
    print("Produto não encontrado.")