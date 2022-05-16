a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
enesimo = a1 + r * (10)
for x in range(a1,enesimo, r):
    print("{} =>".format(x), end=(" "))
print("ACABOU!")
