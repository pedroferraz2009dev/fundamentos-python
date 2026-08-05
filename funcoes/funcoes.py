def exibir_mensagem():
    print("Vai Corinthians!!\n"*10)


def somar():
    valor1 = 50
    valor2 = 60
    soma = valor1 + valor2
    print(f"A soma vale {soma}")


def calcular_media():
        nota1 =float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        return media

exibir_mensagem()
somar()

nota_final = calcular_media()
print(f"A nota final do aluno foi {nota_final}")
