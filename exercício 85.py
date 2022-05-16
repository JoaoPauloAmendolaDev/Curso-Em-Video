lista = []
dados = {}
soma = 0
lista_gols = []
total_gols = 0
while True:
    dados['Nome'] = str(input("Nome: "))
    dados['Jogos'] = int(input("Partidas jogadas: "))
    for x in range(0, dados.get('Jogos'), 1):
        dados['Gols'] = int(input(f"Quantos gols foi feito na partida {x+1}: "))
        lista_gols.append(dados['Gols'])
    lista.append(dados)
    print(lista)
    break

print('=-'*30)
for k, v in dados.items():
    print(f'No campo {k} tem o valor {v}')
    print(total_gols)
    if k == dados["Gols"]:
        total_gols = sum(v)
print('=-'*30)
print(total_gols)
for k, v in enumerate(lista_gols):
    print(f'No jogo {k+1} o jogador {dados["Nome"]} marcou : {v}')