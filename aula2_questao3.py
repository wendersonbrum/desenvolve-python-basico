#Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. Ou seja, 
#ao final v1 terá o valor de v2, e v2 o valor de v1. Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos 
#valores diretamente.
v1 = 10
v2 = 20

print("Valores iniciais:")
print("v1 =", v1)
print("v2 =", v2)
v3 = v1
v1 = v2
v2 = v3
print("Valores trocados:")
print("v1 =", v1)
print("v2 =", v2)