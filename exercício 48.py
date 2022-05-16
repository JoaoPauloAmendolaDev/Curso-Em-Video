sexo = input("Digite seu Sexo: ")
while sexo != 'M' and sexo != 'F':
    print("Digite corretamente como mostrado ao lado [M/F].")
    sexo = input("Digite seu sexo: [M/F]")
print("O sexo lido foi {}!".format(sexo))