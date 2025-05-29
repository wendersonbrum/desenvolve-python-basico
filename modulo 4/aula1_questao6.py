n = int(input())
cont = 0
sapo, rato, coelho = 0, 0, 0
while cont < n:
    quantia = int(input())
    tipo = input()
    if tipo == "S": sapo += quantia
    elif tipo == "R": rato += quantia
    elif tipo == "c": coelho += quantia
    cont += 1 

print("total de cobaias:", sapo + rato + coelho)
print("total de sapos:", sapo)
print("total de ratos:", rato)
print("total de coelhos:", coelho)