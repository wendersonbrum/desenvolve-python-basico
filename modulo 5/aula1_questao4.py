from datetime import datetime

data_hora_atual = datetime.now()
formato = "%d/%m/%Y %H:%M:%S"  
data_hora = data_hora_atual.strftime(formato)
print(f"Data e Hora Atuais: {data_hora}")

