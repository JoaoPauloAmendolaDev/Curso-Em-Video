from time import sleep


def contador(n1, n2, n3):
    print("Contando de 1 até 10!")
    for x in range(1, 10, 1):
        sleep(0.2)
        print(x, end=' => ')
    print('FIM')
    print()
    print("Contando de 10 até 0 de 2 em 2!")
    for z in range(10, 0, -2):
        sleep(0.2)
        print(z, end=' => ')
    print('FIM')
    print()
    if n3 < 0:
        n3 *= - 1
    if n1 > n2 and n3 > 0:
        n3 *= - 1
    print(f'Contando de {n1} até {n2} de {n3} em {n3}')
    if n3 == 0:
        print("DIGITE UM VALOR VÁLIDO PARA O PASSO!")
    else:
        for w in range(n1, n2, n3):
            sleep(0.2)
            print(w, end=' => ')
        print('FIM')


n1 = int(input("Início: "))
n2 = int(input("Fim: "))
n3 = int(input("Passo: "))
contador(n1, n2, n3)
