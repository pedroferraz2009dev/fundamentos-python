def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print("Aluno inserido com sucesso!")
    print("Lista de alunos:", alunos)


alunos = ["Ana", "Carlos", "Mariana", "João"]

nome = input("Digite o nome do novo aluno: ")
posicao = int(input("Digite a posição onde deseja inserir: "))

inserir_aluno(alunos, nome, posicao)