import random

def escolhe_palavra():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.readlines()
      
    return random.choice(palavras).strip()

def carrega_enforcado():
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.read().split("\n\n")
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogar():
    palavra = escolhe_palavra()
    estagios = carrega_enforcado()
    letras_acertadas = ["_"] * len(palavra)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao jogo da Forca!")
    print("Palavra:", " ".join(letras_acertadas))
    
    while tentativas > 0 and "_" in letras_acertadas:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if letra in palavra:
            for index, char in enumerate(palavra):
                if char == letra:
                    letras_acertadas[index] = letra
            print("Acertou!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Errou!")
        
        imprime_enforcado(6 - tentativas, estagios)
        print("Palavra:", " ".join(letras_acertadas))
        print(f"Erros: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")
    
    if "_" not in letras_acertadas:
        print("Parabéns! Você ganhou!")
    else:
        print("Você perdeu! A palavra era:", palavra)

jogar()
