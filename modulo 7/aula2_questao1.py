import datetime

def data_por_extenso(data):
    try:
        data_obj = datetime.datetime.strptime(data, '%d/%m/%Y')
        nome_mes = data_obj.strftime('%B')
        dia = data_obj.day
        ano = data_obj.year
        return f"Você nasceu em {dia} de {nome_mes} de {ano}."
    except ValueError:
        return "Formato de data inválido. Use o formato dd/mm/aaaa."

def main():
    data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
    resultado = data_por_extenso(data_nascimento)
    print(resultado)

if __name__ == "__main__":
    main()
