a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
# O primeiro contador é para definir o valor da PA, ou seja, ele é o valor + r
# O segundo contador serve para que o while dure 10 voltas
# O terceiro contador é para definir quantas vezes ele deve ir, sendo inicialmente 11 vezes
# O quarto contador serve para definir quantas vezes o ciclo while aconteceu
contador = a1
contador2 = 0
contador3 = 11
contador4 = 0
while contador2 < contador3:
    if contador == 0:
        print("{} =>".format(a1), end=" ")
    if contador2 != 10:
        print("{} =>".format(contador), end=" ")
        contador += r
    contador2 += 1
    contador4 += 1
    if contador2 == contador3:
        print("PAUSA")
        x = int(input("Quantos termos você deseja mostrar a mais? "))
        contador3 = x
        contador2 = 0
        contador4 += 1
print("FIM\n"
      "Progressão finalizada com {} termos mostrados.".format(contador4))
