contador, soma, x = 0
while x != 999:
    x = int(input("Digite o valor que deseja [DIGITE 999 PARA PARAR]: "))
    contador += 1
    soma += x
    if x == 999:
        soma -= 999
        contador -= 1
        print("Você digitou {} valores, que somados deram {}".format(contador, soma))
