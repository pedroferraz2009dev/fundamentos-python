def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print("Nome adicionado com sucesso!")
    print("Lista de nomes:", nomes)


nomes = []

nome = input("Digite um nome: ")

adicionar_nome(nomes, nome)