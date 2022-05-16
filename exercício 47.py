sexoM = 0
sexoF = 0
idadeFM20 = 0
idadeMedia = 0
idadeM = 0
quantidadeDePessoas = 1
nomeMV = ""
for x in range(0, 4):
    print("----- {}ª PESSOA -----".format(quantidadeDePessoas))
    nome = input("Digite o seu nome: ")
    idade = int(input("digite sua idade: "))
    sexo = input("Digite seu sexo (masculino/feminino): ").lower().strip()
    quantidadeDePessoas += 1
    if sexo == "masculino":
        sexoM += 1
        if idade > idadeM:
            idadeM = idade
            nomeMV = nome
    elif sexo == "feminino":
        sexoF = sexoF + 1
        if idade < 20:
            idadeFM20 += 1
    idadeMedia = idadeMedia + idade
idadeMedia = idadeMedia / 4
if sexoM > 0:
    print("idade do mais velho:  {}, \n"
          "nome do mais velho:  {}".format(idadeM, nomeMV))
if sexoF > 0:
    print("Numero de mulheres {} , \n"
          "quantidade de mulher abaixo de 20 anos: {}".format(sexoF, idadeFM20))
if sexoM <= 0:
    print("Não há homens na pesquisa.")
if sexoF <= 0:
    print("Não há mulheres na pesquisa.")
print("A média de idade é: {:.0f} anos.".format(idadeMedia))