from variaveis.exercicios.exercicio_11 import media


def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["Gustavo", "GH","Ferrazlindo", "Lara deide", "Beltrão"]
mostrar_nomes(lista_de_nomes)


def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nome(lista_de_nomes, "Gustavo")


#adicionar novo nome em uma posição especifica
def adicionar_nome(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posicao {posicao} da lista: {nomes}")

def adicionar_nome_posicao(Liata_de_nomes, nome:"Gustavo", posicao:2):
    Liata_de_nomes.insert(posicao, nome)

# Juntando duas Listas
def Juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes da lista: {novos_nomes} foram inseridos na lista: {nomes}")

novos_nomes = ["Yago", "Marcelo"]
Juntar_nomes(lista_de_nomes,novos_nomes)


# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
     print('Este nome não existe na lista')
    else:
        nomes.remove(nome)
    print(f"O nome {nome} foi removido da lista: {nomes}")

remover_nome_pelo_valor(lista_de_nomes, "Gustavo")

# Removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(5)
    print(f'O nome da posição {posicao} é {nomes[posicao]}, foi removido!')

remover_nome_pelo_indice(lista_de_nomes, "Gustavo")

# Dewcobrind a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome in nomes:
        print("Nome não encontrado!")
    else:
     posicao = nomes.index(nome)
    print(f"A posição do nome {nome} é {posicao}")

encontrar_posicao_pelo_valor(lista_de_nomes, "Gustavo")

#  Contanto elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"A quantidade de nomes da lista é {quantidade}")

quantidade_de_nomes(lista_de_nomes)

# Ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(lista_de_nomes)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")

    ordenar_nomes(lista_de_nomes)

# Operações matemática
# Calcular média
def calcular_média(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A média das notas é {media}")

notas_semestres = [7.8, 6.5, 9, 8.7, 9.5]
calcular_média(notas_semestres)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    notas_ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return notas_ordenadas, media

notas_ordenadas, batata = gerenciar_notas(notas_semestres, [3.5])
print(f"notas ordenadas: {notas_ordenadas}")
print(f"A média das notas é {batata}")

# Lista de listas
def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f'Minha lista de produtos: {produtos[0][2]}')

Lista_produtos = [
    ["Arroz",2, 32.00],
    ["Feijão",3, 8.50]
]
novo_produtos = []
adicionar_produto(Lista_produtos, novo_produto)


def quantidade_total_produtos(produtos):
    quantidade = []

    for produto in produtos:
        print(f'rodando laço for em lista_produtos: {produto[1]}')
        quantidade.append(produto[1])

    return sum(quantidade)

quantidade_produtos = quantidade_total_produtos(Lista_produtos)
print(f'Quantidade total de produtos é {quantidade_produtos}')

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valores.append(produto[2])

    return sum(valores)

preco_total_produtos = valor_total_produtos(Lista_produtos)
print(f'O valor total dos produtos é {preco_total_produtos}')