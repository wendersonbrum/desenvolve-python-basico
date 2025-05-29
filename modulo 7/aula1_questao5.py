frase = input("Digite uma frase: ")

contador_vogais = 0
indices_vogais = []
vogais = "aeiouAEIOU"

for indice, caractere in enumerate(frase):
    if caractere in vogais:
        contador_vogais += 1
        indices_vogais.append(indice)

print(f"{contador_vogais} vogais")
print(f"Índices {indices_vogais}")
