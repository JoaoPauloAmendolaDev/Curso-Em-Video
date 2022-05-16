from _datetime import date
nascimento = int(input("Digite sua idade para definição de categoria: "))
data = date.today().year
idade = data - nascimento
if idade <= 9:
    print("Sua categoria é MIRIM.")
elif idade <= 14:
    print("Sua categoria é INFANTIL.")
elif idade <= 19:
    print("Sua categoria é JÚNIOR.")
elif idade <= 25:
    print("Sua categoria é SÊNIOR.")
else:
    print("Sua categoria é MASTER.")
