from datetime import date
idade = int(input("Digite em qual ano você nasceu: "))
ano = date.today().year
if ano - idade < 18:
    alistamento = 18 - (ano - idade)
    print("Você ainda é muito jovem, faltam {} ano/anos para você se alistar.".format(alistamento))
elif ano - idade > 18:
    alistamento = ano - 18 - idade
    print("Você passou da época, está {} ano/anos atrasado".format(alistamento))
else:
    print("Você está na idade certa, vá se alistar!")
