def obter_lista(tamanho, numero_lista):
    lista = []
    print(f"Digite os {tamanho} elementos da lista {numero_lista}:")
    for _ in range(tamanho):
        elemento = int(input())
        lista.append(elemento)
    return lista

def combinar_listas(lista1, lista2):
    combinada = []
    len1, len2 = len(lista1), len(lista2)
    min_len = min(len1, len2)
    for i in range(min_len):
        combinada.append(lista1[i])
        combinada.append(lista2[i])
    if len1 > len2:
        combinada.extend(lista1[min_len:])
    else:
        combinada.extend(lista2[min_len:])
    
    return combinada

def main():
    tamanho1 = int(input("Digite a quantidade de elementos da lista 1: "))
    lista1 = obter_lista(tamanho1, 1)
    tamanho2 = int(input("Digite a quantidade de elementos da lista 2: "))
    lista2 = obter_lista(tamanho2, 2)
    lista_intercalada = combinar_listas(lista1, lista2)
    print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))

if __name__ == "__main__":
    main()
