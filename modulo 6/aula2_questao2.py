import random

def main():
    num_elementos = random.randint(5, 20)
    elementos = [random.randint(1, 10) for _ in range(num_elementos)]
    soma_elementos = sum(elementos)
    media_elementos = round(soma_elementos / num_elementos, 2)
    print("Lista de elementos:", elementos)
    print("Soma dos valores da lista:", soma_elementos)
    print("Média dos valores da lista:", media_elementos)

if __name__ == "__main__":
    main()
