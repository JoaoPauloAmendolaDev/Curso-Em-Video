n1 = int(input("Digite o valor da primeira reta: "))
n2 = int(input("Digite o valor da segunda reta: "))
n3 = int(input("Digite o valor da terceira reta: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print("Essas retas podem formar um triângulo!")
else:
    print("Essas retas não podem formar um triângulo!")



