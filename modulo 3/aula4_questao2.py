#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que 
#solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente
# à classificação do filme:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."
avaliaçao = int(input("Avalie o filme em uma escala de 1 a 5"))
if avaliaçao == 5:
    retorno = "Excelente!"
elif avaliaçao == 4:
    retorno = "Muito bom!"
elif avaliaçao == 3:
    retorno = "Bom!"
elif avaliaçao == 2:
    retorno = "Regular."
else:
    retorno = "Ruim."

print({retorno})


