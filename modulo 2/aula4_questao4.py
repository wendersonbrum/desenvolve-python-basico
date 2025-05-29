valor = int(input("Digite o valor: "))
nota_100 = valor // 100
valor = valor % 100 # % é o resto da divisão 

nota_50 = valor // 50
valor = valor % 50

nota_20 = valor // 20  
valor = valor % 20

nota_10 = valor // 10  
valor = valor % 10

nota_5 = valor // 5  
valor = valor % 5

nota_2 = valor // 2  
valor = valor % 2

nota_1 = valor 
print(f"{nota_100} notas de 100")
print(f"{nota_50} notas de 50")
print(f"{nota_20} notas de 20")
print(f"{nota_10} notas de 10")
print(f"{nota_5} notas de 5")
print(f"{nota_2} notas de 2")

