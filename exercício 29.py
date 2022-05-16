n1 = float(input("Digite o valor do primeiro número: "))
n2 = float(input("Digite o valor do segundo número: "))
if n1 > n2:
    print("O número {} é o maior.".format(n1))
elif n2 > n1:
    print("O número {} é o maior.".format(n2))
else:
    print("Os valores são iguais.")
