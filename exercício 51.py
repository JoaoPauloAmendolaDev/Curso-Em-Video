n1 = int(input("Digite um número inteiro: "))
contador = n1
valor = 1
print("Calculando {}! = ".format(n1), end="")
while contador > 0:
    print("{}".format(contador), end="")
    print(" x " if contador > 1 else " = ", end="")
    valor *= contador
    contador -= 1
print(valor)
