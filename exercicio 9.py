import random
n1 = input("Digite o nome de um aluno: ")
n2 = input("Digite o nome de um aluno: ")
n3 = input("Digite o nome de um aluno: ")
n4 = input("Digite o nome de um aluno: ")
sorteado = random.choice([n1, n2, n3, n4])
print("Você irá limpar o quadro {}!".format(sorteado))
