def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    if nota in notas:
        notas.remove(nota)
        print("Nota removida com sucesso!")
    else:
        print("Nota não encontrada.")


def media_notas(notas):
    if len(notas) > 0:
        return sum(notas) / len(notas)
    else:
        return 0


notas = [7.0, 8.5, 6.0]

nova_nota = float(input("Digite uma nova nota: "))
adicionar_nota(notas, nova_nota)

print("Notas:", notas)

nota_remover = float(input("Digite a nota que deseja remover: "))
remover_nota(notas, nota_remover)

print("Notas atualizadas:", notas)

media = media_notas(notas)

print("Média das notas:", media)