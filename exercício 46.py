var1 = 1
listacriada = []
for x in range(0, 5):
    peso = int(input("Digite o peso da {} ª pessoa: ".format(var1)))
    var1 += 1
    listacriada.append(peso)
    listacriada.sort()
print("a pessoa mais pesada pesa {}Kg.".format(listacriada[4]))
print("A pessoa mais leve pesa {}Kg.".format(listacriada[0]))
