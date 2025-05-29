
# Implemente aqui sua solução
def imprime_vogais_indices(frase):
    vogais = 'aeiou'
    for indice, caractere in enumerate(string):
        if caractere.lower() in vogais:
            print(f"Vogal: {caractere}, Índice: {indice}")

frase = "O rato roeu a roupa da Alice"

imprime_vogais_indices(frase)


