#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
#Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas.
#O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = int(input("Informe a distância de entrega em km:"))
peso = float(input("Informe o peso do pacote:"))
if distancia <= 100:
    if peso > 10:
        preço = float(10 + (distancia * peso))
    else:
        preço = float(distancia * peso)

elif distancia > 100 and distancia < 300:
    if peso > 10:
        preço = float(10 + (distancia * 1.5) * peso )
    else:
        preço = float((distancia * 1.5)* peso )

elif distancia > 300:
    if peso > 10:
        preço = float(10 + (distancia * 2)* peso )
    else:
        preço = float((distancia * 2)* peso )


print("O valor do frete é:", preço)
        