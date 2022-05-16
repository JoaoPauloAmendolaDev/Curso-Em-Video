contadorsexoM = contadorsexoFm20 = contadoridade18mais = 0
while True:
    nome = input("Digite um Nome: ")
    sexo = input("Digite o Sexo [M/F]: ").upper().strip()[0]
    idade = int(input("Digite a idade: "))
    if idade > 18:
        contadoridade18mais += 1
    if sexo == "M":
        contadorsexoM += 1
    if sexo == "F" and idade < 20:
        contadorsexoFm20 += 1
    continuar = input("Você deseja continuar? [S/N]: ").upper().strip()[0]
    if continuar == "N":
        print("{} Pessoas tem mais de 18 anos.\n"
              "{} Homens foram cadastrados.\n"
              "{} Mulheres tem menos de 20 anos.".format(contadoridade18mais, contadorsexoM, contadorsexoFm20))
        break