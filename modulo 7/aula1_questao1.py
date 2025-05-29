def escada_com_nome(nome):
    for i in range(1, len(nome) + 1):
        print(nome[:i])

nome = input("Digite seu nome: ")
escada_com_nome(nome)
