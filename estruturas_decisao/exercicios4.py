def verificar_nota():
    nota = float(input("Digite a nota do aluno: "))

    if nota >= 6:
        print("Aprovado")
    elif nota < 6:
        print("Reprovado")
    else:
        print("Nota inválida")


verificar_nota()