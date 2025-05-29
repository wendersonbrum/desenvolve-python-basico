
def primeiras_linhas(arquivo, n=25):
    with open(arquivo, 'r', encoding='utf-8') as file:
        for i, linha in enumerate(file):
            if i < n:
                print(linha, end='')
            else:
                break

def n_linhas(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        num_linhas = sum(1 for _ in file)
    print(f"O arquivo tem {num_linhas} linhas.")

def maior_linha(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        linha_maior = ''
        for linha in file:
            if len(linha) > len(linha_maior):
                linha_maior = linha
    print("Linha com mais caracteres:")
    print(linha_maior)

def ocorrencias(arquivo, palavra):
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read().lower()
        contagem = conteudo.count(palavra.lower())
    print(f'A palavra "{palavra}" foi mencionada {contagem} vezes.')


primeiras_linhas('estomago.txt')
n_linhas ('estomago.txt')
maior_linha('estomago.txt')
ocorrencias('estomago.txt', 'Nonato')
ocorrencias('estomago.txt', 'Íria')
