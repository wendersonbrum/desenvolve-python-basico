import random

def embaralhar_palavras(frase):
    # Dividir a frase em palavras
    palavras = frase.split()
    # Lista para armazenar as palavras embaralhadas
    palavras_embaralhadas = []
    
    for palavra in palavras:
        if len(palavra) > 2:  # Embaralhar apenas se a palavra tiver mais de 2 letras
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])
            # Embaralhar as letras internas
            random.shuffle(letras_internas)
            # Formar a palavra embaralhada
            palavra_embaralhada = primeira_letra + ''.join(letras_internas) + ultima_letra
        else:
            palavra_embaralhada = palavra  # Manter palavras com 2 ou menos letras inalteradas
        
        palavras_embaralhadas.append(palavra_embaralhada)
    
    # Juntar as palavras embaralhadas de volta em uma frase
    frase_embaralhada = ' '.join(palavras_embaralhadas)
    return frase_embaralhada

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
