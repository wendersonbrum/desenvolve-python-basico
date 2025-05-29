import csv
import os



class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.codigo},{self.nome},{self.preco},{self.quantidade}"

def carregar_produtos(arquivo):
    produtos = []
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                produtos.append(Produto(linha[0], linha[1], float(linha[2]), int(linha[3])))
    return produtos

def salvar_produtos(produtos, arquivo):
    with open(arquivo, 'w', newline='') as f:
        escritor = csv.writer(f)
        for produto in produtos:
            escritor.writerow([produto.codigo, produto.nome, produto.preco, produto.quantidade])

def adicionar_produto(produtos, codigo, nome, preco, quantidade):
    produtos.append(Produto(codigo, nome, preco, quantidade))

def listar_produtos(produtos):
    for produto in produtos:
        print(produto)

def buscar_produto(produtos, criterio):
    for produto in produtos:
        if produto.codigo == criterio or produto.nome.lower() == criterio.lower():
            print(f"Produto encontrado: {produto}")
            return produto
    print("Produto não encontrado.")
    return None

def atualizar_produto(produtos, codigo, nome=None, preco=None, quantidade=None):
    for produto in produtos:
        if produto.codigo == codigo:
            if nome is not None:
                produto.nome = nome
            if preco is not None:
                produto.preco = preco
            if quantidade is not None:
                produto.quantidade = quantidade
            return True
    return False

def remover_produto(produtos, codigo):
    for produto in produtos:
        if produto.codigo == codigo:
            produtos.remove(produto)
            return True
    return False

def imprimir_produtos_por_nome(produtos):
    for produto in sorted(produtos, key=lambda p: p.nome):
        print(produto)

def imprimir_produtos_por_preco(produtos):
    for produto in sorted(produtos, key=lambda p: p.preco):
        print(produto)

def autenticar_usuario():
    while True:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha do usuário: ")
        if usuario == "admin" and senha == "123456":
            return "admin"
        elif usuario == "user" and senha == "654321":
            return "user"
        else:
            print("Credenciais inválidas. Tente novamente.")

def main():
    arquivo = 'produtos.csv'
    produtos = carregar_produtos(arquivo)

    nivel_permissao = autenticar_usuario()
    print(f"Bem vindo! {nivel_permissao}")

    while True:
        print("\nMenu:")
        if nivel_permissao == 'admin':
            print("1. Adicionar Produto")
            print("2. Listar Produtos")
            print("3. Buscar Produto")
            print("4. Atualizar Produto")
            print("5. Remover Produto")
            print("6. Sair")
        else:
            print("1. Listar Produtos")
            print("2. Buscar Produto")
            print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if nivel_permissao == 'admin':
            if opcao == '1':
                codigo = input("Digite o código do produto: ")
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                adicionar_produto(produtos, codigo, nome, preco, quantidade)
                salvar_produtos(produtos, arquivo)
                print("Produto adicionado.")

            elif opcao == '2':
                print("\nLista de Produtos:")
                listar_produtos(produtos)

            elif opcao == '3':
                criterio = input("Digite o código ou nome do produto para buscar: ")
                buscar_produto(produtos, criterio)

            elif opcao == '4':
                codigo = input("Digite o código do produto a ser atualizado: ")
                nome = input("Novo nome (deixe em branco para não alterar): ")
                preco = input("Novo preço (deixe em branco para não alterar): ")
                quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
                if preco:
                    preco = float(preco)
                else:
                    preco = None
                if quantidade:
                    quantidade = int(quantidade)
                else:
                    quantidade = None
                if atualizar_produto(produtos, codigo, nome if nome else None, preco, quantidade):
                    salvar_produtos(produtos, arquivo)
                    print("Produto atualizado.")
                else:
                    print("Produto não encontrado.")

            elif opcao == '5':
                codigo = input("Digite o código do produto a ser removido: ")
                if remover_produto(produtos, codigo):
                    salvar_produtos(produtos, arquivo)
                    print("Produto removido.")
                else:
                    print("Produto não encontrado.")
            elif opcao == '6':
                break

            else:
                print("Opção inválida.")

        else:
            if opcao == '1':
                print("\nLista de Produtos:")
                listar_produtos(produtos)

            elif opcao == '2':
                criterio = input("Digite o código ou nome do produto para buscar: ")
                buscar_produto(produtos, criterio)

            elif opcao == '3':
                break

            else:
                print("Opção inválida.")

if __name__ == '__main__':
    main()
