def remover_produto(produtos, produto):
    if produto in produtos:
        produtos.remove(produto)
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")

    print("Produtos:", produtos)


produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]

produto = input("Digite o produto que deseja remover: ")

remover_produto(produtos, produto)