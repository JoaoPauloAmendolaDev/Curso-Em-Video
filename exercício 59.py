from random import randint

contador = 0
while True:
    print("=" * 20)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=" * 20)
    n1 = int(input("Digite um valor: "))
    decisao = input("Será par ou será impar? [P/I] ").upper().strip()[0]
    n2 = randint(0, 9)
    n3 = n1 + n2
    if n3 % 2 == 0 and decisao == "P":
        print("Você VENCEU!!\n"
              "Você escolheu {} e o computador {}. Total de {} DEU PAR!".format(n1, n2, n3))
        contador += 1
    elif n3 % 2 == 0 and decisao == "I":
        print("Você PERDEU!!\n"
              "Você escolheu {} e o computador {}. Total de {} DEU PAR!".format(n1, n2, n3))
        print("Você ganhou por {}x seguidas!".format(contador))
        break
    elif n3 % 2 == 1 and decisao == "I":
        print("Você VENCEU!!\n"
              "Você escolheu {} e o computador {}. Total de {} DEU IMPAR!".format(n1, n2, n3))
        contador += 1
    elif n3 % 2 == 1 and decisao == "P":
        print("Você PERDEU!!\n"
              "Você escolheu {} e o computador {}. Total de {} DEU IMPAR!".format(n1, n2, n3))
        print("Você ganhou por {}x seguidas!".format(contador))
        break
