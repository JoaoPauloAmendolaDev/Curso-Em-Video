import time
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
x = 0
while x != 5:
    x = int(input(" [1] = SOMAR"
                  "\n [2] = MULTIPLICAR"
                  "\n [3] = MAIOR"
                  "\n [4] = NOVOS NÚMEROS"
                  "\n [5] = SAIR DO PROGRAMA"
                  "\n Digite a opção escolhida: "))
    if x == 1:
        n3 = n1 + n2
        print("A soma é: {}".format(n3))
        time.sleep(3)
    if x == 2:
        n3 = n1 * n2
        print("A multiplicação deles é: {}".format(n3))
        time.sleep(3)
    if x == 3:
        if n1 > n2:
            print("O maior é: {}".format(n1))
        if n2 > n1:
            print("O maior é: {}".format(n2))
        if n1 == n2:
            print("Os números são iguais.")
        time.sleep(3)
    if x == 4:
        n1 = float(input("Digite um novo número: "))
        n2 = float(input("Digite um novo número: "))
        time.sleep(3)
print("Fim do programa")
