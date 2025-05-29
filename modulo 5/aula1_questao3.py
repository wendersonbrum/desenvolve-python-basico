import random

numero = random.randint(1, 10)
n = int(input("Escreva um número de 1 a 10: "))
if n < numero:
    print("Muito baixo! O número correto é ", numero)
elif n > numero:
    print("Muito alto! O número correto é ", numero)
else:
    print("Você adivinhou o número.")


