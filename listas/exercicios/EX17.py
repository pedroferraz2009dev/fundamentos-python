def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print("Produto vendido com sucesso!")
    else:
        print("Produto não está disponível.")

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

print("Estoque:", estoque)

produto = input("Digite o produto que deseja vender: ")

estoque = vender_produto(estoque, produto)

print("Estoque atualizado:", estoque)