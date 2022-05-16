import random
entrada = input("Digite pedra, papel ou tesoura: ").strip().lower()
n = random.randrange(0, 2)
itens = ("pedra", "papel", "tesoura")
"""if n == 0:
    print("Você venceu!")
elif n == 1:
    print("Você perdeu!")
elif n == 2:
    print("Empate!")"""
if entrada == "pedra":
    entrada = 0
    if n == 0:
        print("EMPATE!")
    if n == 1:
        print("VOCÊ PERDEU, O COMPUTADOR ESCOLHEU PAPEL!")
    if n == 2:
        print("VOCÊ VENCEU, O COMPUTADOR ESCOLHEU TESOURA!")
elif entrada == "papel":
    entrada == 1
    if n == 1:
        print("EMPATE!")
    if n == 0:
        print("VOCÊ VENCEU,O COMPUTADOR ESCOLHEU PEDRA!")
    if n == 2:
        print("VOCÊ PERDEU,O COMPUTADOR ESCOLHEU TESOURA!")
elif entrada == "tesoura":
    entrada == 2
    if n == 2:
        print("EMPATE!")
    if n == 0:
        print("VOCÊ PERDEU, O COMPUTADOR ESCOLHEU PEDRA!")
    if n == 1:
        print("VOCÊ VENCEU, O COMPUTADOR ESCOLHEU PAPEL!")
else:
    print("Digite pedra, papel ou tesoura apenas.")
#Dois modos de fazer, um complicado e um simples, os dois fazem a mesma coisa já que
#é totalmente dependente de sorte e não há nenhum tipo de estratégia.
