from _datetime import date
var1 = 0
var2 = 0
pessoas = 1
data = date.today().year
for x in range(0,7):
    idade = int(input("Qual ano a {}ª pessoa nasceu: ".format(pessoas)))
    pessoas = pessoas+1
    ano = data - idade
    if ano >= 18:
        var2 = var2 + 1
    else:
        var1 = var1 + 1
print("a quantidade de pessoas maior de idade é: {}\n"
      "e a quantidade de menores de idade é: {}".format(var2, var1))

