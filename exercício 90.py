import random
def sorteia(a):
    for x in range(0, 5):
        a.append(random.randint(0, 10))
    print(f'Os valores sorteados são: {a}')
def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


lista = []
sorteia(lista)
soma_par(lista)





