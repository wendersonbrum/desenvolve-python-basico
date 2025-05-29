def extrair_dominios(urls):
    dominios = []
    for url in urls:
        dominio = url[4:-4]  
        dominios.append(dominio)
    return dominios

def main():
    urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
    dominios = extrair_dominios(urls)
    print("URLs:", urls)
    print("dominios:", dominios)

if __name__ == "__main__":
    main()
