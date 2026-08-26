def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    if len(fila) > 0:
        return fila.pop(0)
    else:
        return None


fila = []

while True:
    cliente = input("Digite o nome do cliente (ou 'fim' para parar): ")

    if cliente.lower() == "fim":
        break

    adicionar_cliente(fila, cliente)

print("\nFila de atendimento:", fila)

while len(fila) > 0:
    cliente_atendido = atender_cliente(fila)
    print("Cliente atendido:", cliente_atendido)

print("Fila vazia!")