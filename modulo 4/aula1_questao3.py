n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
m = ((n1 + n2 + n3 ) / 3)
if m >= 60:
    print("aprovado")
elif m >= 40 and m < 60:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")
