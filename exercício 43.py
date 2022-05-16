n = int(input("digite um valor para verificar se ele é número primo: "))
contador = 0
for x in range(1, n+1):
    if n % x == 0:
        print("\033[33m", end=" ")
        contador = contador + 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(x), end=" ")
if contador == 2:
    print("\nesse número é primo \nele se dividiu {} vezes ".format(x, contador), end=" ")
elif contador != 2:
    print("\nEste número não é primo\n"
          "ele se dividiu {} vezes.".format(contador))
"""if n == 2:
    print("{} é numero primo pois se divide com ele e com 1 apenas.".format(n))
elif n == 3:
    print("{} é numero primo pois se divide com ele e com 1 apenas.".format(n))
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("{} não é um número primo.".format(n))
else:
    print("{} é um número primo.".format(n))"""
