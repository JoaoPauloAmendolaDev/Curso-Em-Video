from operator import itemgetter
dic = []
nome = {}
media = {}
while True:
    nome["nome"] = str(input("Nome: "))
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    media['media'] = (n1 + n2) / 2
    dic.append(nome.copy())
    dic.append(media.copy())
    cont = input("Deseja continuar?: [S/N] ").strip().lower()[0]
    if cont == 'n':
        break
for x in dic:
    for chave, valor in x.items():
        print(f'{chave}: {valor}', end=' ')
    print()
