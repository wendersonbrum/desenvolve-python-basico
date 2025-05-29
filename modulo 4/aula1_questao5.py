n = int(input("quantos participantes?"))
soma = 0
cont = 0
while cont < n:
    idade = int(input("Digite a idade"))
    soma += idade 
    cont += 1 
print(soma)
print(f"a média é {soma/n: .0f} anos")
