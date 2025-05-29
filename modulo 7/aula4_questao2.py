import re

def process_text_file(input_file, output_file):
   
    with open('frase.txt', 'r', encoding='utf-8') as file:
        text = file.read()

   
    words = re.findall(r'\b[a-zA-Z]+\b', text)


    with open(output_file, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

    with open(output_file, 'r', encoding='utf-8') as file:
        print(file.read())


process_text_file('arquivo.txt', 'palavras.txt')