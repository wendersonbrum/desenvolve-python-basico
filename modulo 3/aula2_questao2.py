# Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

juliana = int(input("Digite a idade de Juliana: "))
cris = int(input("Digite a idade de Cris: "))

liberado = juliana > 17 or cris > 17
print(liberado)
