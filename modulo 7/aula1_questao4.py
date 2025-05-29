numero = input("Digite o número: ")

if len(numero) == 8:
    numero_completo = "9" + numero[:4] + "-" + numero[5:]
elif len(numero) == 9:
    if numero[0] == "9":
        numero_completo = numero[:5] + "-" + numero[5:]
    else:
        numero_completo = numero[:5] + "-" + numero[5:]
else:
    print("Número de celular inválido. Deve ter 8 ou 9 dígitos.")
    exit()

print(f"Número completo: {numero_completo}")
