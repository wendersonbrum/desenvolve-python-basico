import random

def encontrar_intervalo_maior_negativos(lista):
    max_negativos = 0
    melhor_inicio = 0
    melhor_fim = 0
    
    for inicio in range(len(lista)):
        for fim in range(inicio + 1, len(lista) + 1):
            sublista = lista[inicio:fim]
            count_negativos = sum(1 for x in sublista if x < 0)
            if count_negativos > max_negativos:
                max_negativos = count_negativos
                melhor_inicio = inicio
                melhor_fim = fim
    
    return melhor_inicio, melhor_fim

def main():
    lista = [random.randint(-10, 10) for _ in range(20)]
    inicio, fim = encontrar_intervalo_maior_negativos(lista)
    print("Original:", lista)
    del lista[inicio:fim]
    print("Editada:", lista)

if __name__ == "__main__":
    main()
