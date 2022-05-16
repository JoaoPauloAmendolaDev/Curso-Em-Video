lista = []
dados = {}
soma = 0
lista_gols = []
while True:
    dados['Nome'] = str(input("Nome: "))
    dados['Jogos'] = int(input("Partidas jogadas: "))
    for x in range(0, dados.get('Jogos'), 1):
        dados['Gols'] = int(input(f"Quantos gols foi feito na partida {x+1}: "))
        soma += dados['Gols']
        lista_gols.append(dados['Gols'])
    dados['Gols'] = soma
    lista.append(dados)
    print(lista)
    break
print('=-'*30)
for k, v in dados.items():
    print(f'No campo {k} tem o valor {v}')
print('=-'*30)
for k, v in enumerate(lista_gols):
    print(f'No jogo {k+1} o jogador {dados["Nome"]} marcou : {v}')



