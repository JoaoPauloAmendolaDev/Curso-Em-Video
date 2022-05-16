import math
n1 = float(input("Digite um angulo para mostrar seu seno, cosseno e tangente: "))
seno = math.sin(math.radians(n1))
coss = math.cos(math.radians(n1))
tang = math.tan(math.radians(n1))
print("O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(seno, coss, tang))
