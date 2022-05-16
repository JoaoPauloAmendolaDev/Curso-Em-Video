x: int = int(input("Digite o valor a ser sacado: "))
contador1 = 1
contador10 = 10
contador20 = 20
contador50 = 50
total1 = total10 = total20 = total50 = 0
while True:
    if x >= 50:
        x -= 50
        total50 += 1
    elif x >= 20:
        x -= 20
        total20 += 1
    elif x >= 10:
        x -= 10
        total10 += 1
    elif x >= 1:
        x -= 1
        total1 += 1
    elif x == 0:
        break
print("Você receberá\n"
      "{} notas de 50\n"
      "{} notas de 20\n"
      "{} notas de 10\n"
      "{} notas de 1".format(total50, total20, total10, total1))

