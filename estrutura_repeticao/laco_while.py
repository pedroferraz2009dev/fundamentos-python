def mostrar_numero_while():
    contador = 0
    while contador < 10:
        contador += 1
        print(f'contagem atual: {contador}')

mostrar_numero_while()

def contagem_regressiva():
    valor_contagem = int(input('Digite um numero maior que 10: '))
    if valor_contagem < 10:
        print('Valor invalido!')
    else:
        while valor_contagem >= 1:
            print(f'contagem regressiva: {valor_contagem}')
            valor_contagem -= 1
        print("DECOLAnDO!!!")

#contagem_regressiva()

def soma_com_while():
    while True:
        num_1 = int(input('Digite o primeiro valor: '))
        num_2 = int(input('Digite o segundo valor: '))

        if num_1 == 0:
            print('funçao de soma errada!')
            break
        else:
            soma = num_1 + num_2
            print(f"O resultados da soma é {soma}")

#soma_com_while()