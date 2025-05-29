import random
import math

n = int(input("quantos números deseja? "))
valores_aleatorios = [random.randint(0, 100) for _ in range(n)]
soma = sum(valores_aleatorios)
raiz_quadrada = math.sqrt(soma)
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")

