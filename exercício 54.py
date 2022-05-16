quantidade = int(input("Digite quantos elementos você quer: "))
n1 = 1
n2 = 1
contador = 3
print("0 => 1 => 1 => ", end="")
while contador < quantidade:
    contador += 1
    n3 = n1 + n2
    print(n3, end=(" => "))
    n1 = n2
    n2 = n3
else:
    print("FIM")