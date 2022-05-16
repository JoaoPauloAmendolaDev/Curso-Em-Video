x = (int(input("Digite um valor: ")),
     int(input("Digite um valor: ")),
     int(input("Digite um valor: ")),
     int(input("Digite um valor: ")))
if 9 in x:
    print("O número 9 aparece {} vezes".format(x.count(9)))
else:
    print("Não há o número 9 na sua lista.")
if 3 in x:
    print("O número 3 aparece na posição {}".format(x.index(3)+1))
else:
    print("O número 3 não aparece na lista.")
print("Os valores digitados pares foram", end=" ")
for n in x:
    if n % 2 == 0:
        print("{}".format(n), end=" ")

