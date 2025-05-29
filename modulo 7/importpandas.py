import csv

# Ler o arquivo CSV
with open('spotify-2023.csv', mode='r', encoding='latin-1') as file:
    reader = csv.reader(file)
    
    # Converter o objeto reader em uma lista de linhas
    rows = list(reader)

# Exibir as linhas
for row in rows:
    print(row)