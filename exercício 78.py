from random import randint
lista = []
jogos = []
contadorcondicional = contadorjogo = 0
while True:
    num = int(input("Quantos jogos você deseja gerar?: "))
    for c in range(0, num, 1):
        for x in range(0, 6, 1):
            aleatorio = randint(1, 60)
            lista.append(aleatorio)
        jogos.append(lista[:])
        print(f'{jogos[contadorjogo]}')
        contadorjogo += 1
        lista.clear()
    print(jogos)

