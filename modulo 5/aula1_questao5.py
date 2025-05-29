import emoji

def exibir_lista_de_emojis(emojis):
    print("Lista de Emojis Disponíveis:")
    for emoji, texto in emojis.items():
        print(f"{emoji}: {texto}")

def main():
    emojis = {
        "👍": "like",
        "🌞": "sun",
        "🌈": "rainbow",
        "🤠": "cowboy_hat_face",
        "😎": "smiling_face_with_sunglasses",
        "🍀": ":four_leaf_clover",
    }
    exibir_lista_de_emojis(emojis)
if __name__ == "__main__":
    main()
frase = (input("Digite uma frase para ser emojizada: "))

print(emoji.emojize(frase))
