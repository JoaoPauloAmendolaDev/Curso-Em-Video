soma = contador = x = 0
while True:
    z = int(input("Digite o valor que você deseja (999 para parar): "))
    if z == 999:
        break
    contador += 1
    soma += z
print("Você digitou {} números\n"
      "Esses números somados deram {}\n".format(contador, soma))
