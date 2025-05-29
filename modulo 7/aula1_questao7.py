import random

def encrypt(nomes):
    # Gerar um número aleatório entre 1 e 10
    chave_aleatoria = random.randint(1, 10)
    
    # Lista para armazenar os nomes criptografados
    nomes_criptografados = []
    
    # Iterar sobre cada nome na lista
    for nome in nomes:
        nome_criptografado = []
        for char in nome:
            # Verificar se o caractere está no intervalo visível (33 a 126)
            if 33 <= ord(char) <= 126:
                novo_char = chr(ord(char) + chave_aleatoria)
            else:
                novo_char = char
            nome_criptografado.append(novo_char)
        
        # Juntar os caracteres criptografados de volta em uma string
        nome_criptografado = ''.join(nome_criptografado)
        
        # Adicionar o nome criptografado à lista
        nomes_criptografados.append(nome_criptografado)
    
    # Retornar os nomes criptografados e a chave aleatória gerada
    return nomes_criptografados, chave_aleatoria

# Exemplo de uso:
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_aleatoria = encrypt(nomes)
print("nomes_cript =", nomes_criptografados)
print("chave_aleatoria =", chave_aleatoria)
