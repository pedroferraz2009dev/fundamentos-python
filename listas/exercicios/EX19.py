def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    if nota in notas:
        notas.remove(nota)


def remover_ultima(notas):
    if len(notas) > 0:
        return notas.pop()


def encontrar_nota(notas, nota):
    if nota in notas:
        return notas.index(nota)
    return -1


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def notas_inversas(notas):
    return list(reversed(notas))


def somar_notas(notas):
    return sum(notas)


def calcular_media(notas):
    return sum(notas) / len(notas)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

print("Notas iniciais:", notas)

# 1. Adicionar uma nota
adicionar_nota(notas, 8.0)
print("\n1 - Após adicionar nota:", notas)

# 2. Inserir uma nota
inserir_nota(notas, 10.0, 2)
print("2 - Após inserir nota na posição 2:", notas)

# 3. Adicionar várias notas
adicionar_varias_notas(notas, [6.5, 7.0])
print("3 - Após adicionar várias notas:", notas)

# 4. Remover uma nota
remover_nota(notas, 5.5)
print("4 - Após remover 5.5:", notas)

# 5. Remover a última nota
removida = remover_ultima(notas)
print("5 - Última nota removida:", removida)
print("   Lista:", notas)

# 6. Encontrar posição
posicao = encontrar_nota(notas, 8.5)
print("6 - Posição da nota 8.5:", posicao)

# 7. Quantidade de notas
quantidade = quantidade_notas(notas)
print("7 - Quantidade de notas:", quantidade)

# 8. Ordenar notas
ordenadas = ordenar_notas(notas)
print("8 - Notas ordenadas:", ordenadas)

# 9. Mostrar notas em ordem inversa
inversas = notas_inversas(notas)
print("9 - Notas em ordem inversa:", inversas)

# 10. Soma das notas
soma = somar_notas(notas)
print("10 - Soma das notas:", soma)

# 11. Média da turma
media = calcular_media(notas)
print("11 - Média da turma:", media)