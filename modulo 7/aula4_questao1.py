def salvar_frase_em_arquivo(frase):
    caminho_arquivo = "frase.txt"
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(frase)
    
    return caminho_arquivo

def main():

    frase = input("Digite uma frase: ")
    caminho_arquivo = salvar_frase_em_arquivo(frase)
    print(f"Frase salva em {caminho_arquivo}")
if __name__ == "__main__":
    main()
