import random

n1 = input("Digite o nome do representante do grupo: ")
n2 = input("Digite o nome do representante do grupo: ")
n3 = input("Digite o nome do representante do grupo: ")
n4 = input("Digite o nome do representante do grupo: ")
sorteio = [n1, n2, n3, n4]
random.shuffle(sorteio)
print ("A ordem de apresentação será : {}".format(sorteio))
