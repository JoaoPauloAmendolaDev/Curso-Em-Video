"""from collections import OrderedDict
n = []
parar = 0
while True:
    n.append(int(input("Digite um valor: ")))
    parar = input("Deseja continuar? [S/N]: ").lower().strip()[0]
    if parar == "n":
        break
n = list(OrderedDict.fromkeys(n))
n.sort()
print(f'Esses são os seus valores sem repetições e em ordem.\n'
      f'{n}')"""

n = []
while True:
    n.append(int(input("Digite um valor: ")))
    for x in n:
        z = n.count(x)
        if z > 1:
            n.remove(x)
            print("Não foi possível adicionar.")
    parar = input("Deseja continuar? [S/N]: ").lower().strip()[0]
    if parar == "n":
        break
n.sort()
print(n)
