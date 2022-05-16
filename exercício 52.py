a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
#O primeiro contador é para definir o valor da PA, ou seja, ele é o valor + r
#O segundo contador serve para que o while dure 10 voltas
contador = 0
contador2 = 0
while contador2 < 11:
    if contador == 0:
        contador = a1 + r
        print("{} =>".format(a1), end=" ")
    if contador2 != 10:
        print("{} =>".format(contador), end=" ")
    contador += r
    contador2 += 1
print("FIM")
