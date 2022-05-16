import random
n1 = int(input("Digite um valor entre 0 e 5 e veja se vc acertou:"))
n2 = random.randrange(0,6)
if n1 == n2:
    print("Parabéns, você acertou, o número escolhido pelo PC foi {}!".format(n2))
else:
    print("Você errou, o número escolhido pelo PC foi {}.".format(n2))