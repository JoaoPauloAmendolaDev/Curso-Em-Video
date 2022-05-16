import math
c1 = float(input("Digite o valor do cateto oposto: "))
c2 = float(input("Digite o valor do cateto adjacente: "))
hipo = math.hypot(c1, c2)
print("O comprimento da hipotenusa é: {}".format(hipo))
