import random
from time import sleep
from operator import itemgetter

contador = 0
lista = []
NomeDado = {'Jogador 1': random.randint(1, 6),
            'Jogador 2': random.randint(1, 6),
            'Jogador 3': random.randint(1, 6),
            'Jogador 4': random.randint(1, 6)}
print('Valores Sorteados: ')
for k, v in NomeDado.items():
    print(f'{k} tirou {v} no dado!')
    sleep(1)
ranking = sorted(NomeDado.items(), key=itemgetter(1), reverse=True)
for y in range(0, 4):
    print(f'{contador + 1}ª Lugar foi : {ranking[contador]}')
    contador += 1
