n = int(input("Digite n: "))
maior = 0 
while n > 0:
    x = int(input("digite x: "))
    while x > maior:
        maior = x
        n = n - 1
        break

print(maior)