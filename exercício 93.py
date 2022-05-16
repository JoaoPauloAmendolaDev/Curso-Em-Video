def ficha(jogador='', gols=''):
    if jogador == '' and gols != '':
        print(f'O jogador Desconhecido marcou {gols} gols.')
    elif gols == '' and jogador != '':
        print(f'O jogador {jogador} marcou 0 gols.')
    elif gols == '' and jogador == '':
        print("O jogador <Desconhecido> marcou 0 gols.")
    elif gols != '' and jogador != '':
        print(f"O jogador {jogador} fez {gols} na temporada.")


nome = input("Nome: ")
gol = input("Número de gols: ")
ficha(nome, gol)
