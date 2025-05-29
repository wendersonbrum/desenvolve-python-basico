def obter_numeros():
    lista = []
    while len(lista) < 4:
        numeros = input("Digite um número inteiro (ou 'fim' para terminar): ")
        if numeros.lower() == 'fim' and len(lista) >= 4:
            break
        try:
            numero = int(numeros)
            lista.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    return lista

def main():

    numeros = obter_numeros()
    print("Lista original:", numeros)
    
    print("Os 3 primeiros elementos:", numeros[:3])

    print("Os 2 últimos elementos:", numeros[-2:])
  
    print("Lista invertida:", numeros[::-1])
 
    print("Elementos de índice par:", numeros[::2])
    
    print("Elementos de índice ímpar:", numeros[1::2])

if __name__ == "__main__":
    main()
