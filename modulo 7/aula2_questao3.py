import string

def remover_pontuacao(frase):
    frase_sem_pontuacao = frase.translate(str.maketrans('', '', string.punctuation + ' '))
    return frase_sem_pontuacao.lower()

def verifica_palindromo(frase):
    frase_tratada = remover_pontuacao(frase)
    return frase_tratada == frase_tratada[::-1]

def main():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
 
        if frase.lower() == 'fim':
            print('Programa encerrado.')
            break

        if verifica_palindromo(frase):
            print(f'"{frase}" é um palíndromo')
        else:
            print(f'"{frase}" não é um palíndromo')
if __name__ == "__main__":
    main()
