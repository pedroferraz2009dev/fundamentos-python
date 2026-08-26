def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print("Convidados adicionados!")
    print("Lista de convidados:", convidados)


convidados = ["Pedro", "Lucas"]

novos_convidados = ["Ana", "Mariana", "João"]

adicionar_convidados(convidados, novos_convidados)