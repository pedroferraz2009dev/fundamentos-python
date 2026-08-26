def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)


pontuacoes = [850, 1200, 650, 1500, 1000]

ranking = criar_ranking(pontuacoes)

print("Pontuações:", pontuacoes)
print("Ranking da maior para a menor:", ranking)