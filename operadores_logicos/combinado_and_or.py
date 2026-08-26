#   Operadores and e or

def posso_entrar_no_show_do_veigh():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade? "))
    nome_esta_na_lita = bool(input("Qual a sua nome_esta_na_lita? "))

    posso_entrar = idade >= 18 and nome_esta_na_lita or POSSUI_INGRESSO

    print(f"Vou conseguir entrar no show? {posso_entrar}")

posso_entrar_no_show_do_veigh()