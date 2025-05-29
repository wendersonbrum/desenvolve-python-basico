def sao_anagramas(palavra1, palavra2):
    """ Verifica se duas palavras são anagramas uma da outra """
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
palavra_objetivo_limpa = palavra_objetivo.strip().lower()
anagramas = []

for palavra in frase.split():
    palavra_limpa = palavra.strip().lower()
    if sao_anagramas(palavra_objetivo_limpa, palavra_limpa):
        anagramas.append(palavra)

print(f"Anagramas: {anagramas}")
