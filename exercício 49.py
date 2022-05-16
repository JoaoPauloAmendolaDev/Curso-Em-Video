import _random
import random
n1 = int(input("Digite um número entre 0 e 10 e tentarei adivinhar: "))
n2 = random.randrange(0, 11)
contador = 1
if n1 == n2:
    print("Acertei de primeira!, você disse {} e eu também!".format(n1))
while n2 != n1:
    contador += 1
    n2 = random.randrange(0, 11)
    if n2 == n1:
        print("Foi difícil, tive que tentar {} vezes pra acertar seu número, você venceu =(".format(contador))