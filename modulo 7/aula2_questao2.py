def substituir_vogais_por_asterisco(frase):
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    frase_modificada = ''

    for caractere in frase:
        if caractere in vogais:
            frase_modificada += '*'
        else:
            frase_modificada += caractere

    return frase_modificada

def main():
    frase = input("Digite uma frase: ")
    frase_modificada = substituir_vogais_por_asterisco(frase)
    print(f"Frase modificada: {frase_modificada}")

if __name__ == "__main__":
    main()
