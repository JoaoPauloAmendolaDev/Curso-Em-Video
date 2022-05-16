from _datetime import date

dados = {}
dic = {}
data = date.today().year
while True:
    dados["Nome"] = input("Nome: ")
    nascimento = int(input("Ano de nascimento: "))
    dados['Idade'] = data - nascimento
    dados['Carteira'] = int(input("Carteira de trabalho (0 para não possuí): "))
    break
if dados['Carteira'] != 0:
    dados['Contratacao'] = int(input("Ano de contratação: "))
    dados['Aposentadoria'] = dict.get(dados, 'Contratacao') + 30
    print(f'Nome: {dados["Nome"]}\n'
          f'Idade: {dados["Idade"]}\n'
          f'Carteira: {dados["Carteira"]}'
          f'Ano de contratação: {dados["Contratacao"]}'
          f'Aposentadoria: {dados["Aposentadoria"]}Caso seja seu primeiro emprego.')
else:
    print(f'Nome: {dados["Nome"]}\n'
          f'Idade: {dados["Idade"]}\n'
          f'Carteira: Você não possuí carteira de trabalho.')
