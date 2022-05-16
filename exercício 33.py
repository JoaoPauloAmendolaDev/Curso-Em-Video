n1 = int(input("Digite o valor da primeira reta: "))
n2 = int(input("Digite o valor da segunda reta: "))
n3 = int(input("Digite o valor da terceira reta: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print("Essas retas podem formar um triângulo!")
    if n1 == n2 == n3:
        print("Essas retas formam um triangulo EQUILÁTERO!")
    elif n1 == n2 and n1 != n3 or n2 == n3 and n2 != n1:
        print("Essas retas formam um triângulo ISÓSCELES!")
    elif n1 != n2 and n1 != n3:
        print("Essas retas formam um triângulo ESCALENO!")
else:
    print("Essas retas não podem formar um triângulo!")




