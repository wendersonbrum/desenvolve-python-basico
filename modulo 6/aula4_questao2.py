def main():
    frase = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    vogais_na_frase = [char for char in frase if char in vogais]
    consoantes_na_frase = [char for char in frase if char.isalpha() and char not in vogais]
    vogais_na_frase.sort()
    print("Vogais:", vogais_na_frase)
    print("Consoantes:", consoantes_na_frase)

if __name__ == "__main__":
    main()
