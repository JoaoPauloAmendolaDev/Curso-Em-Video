valor = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o seu salário líquido: "))
anos = int(input("Digite em quantos anos deseja pagar: "))
mensalidade = (anos * 12) / valor
if mensalidade >= 0.3 * salario:
    print("seu empréstimo foi negado, pois você pagaria {:.2f} de mensalidade o que excederia 30% do seu salário liquído.".format(mensalidade))
else:
    print("Seu empréstimo foi aprovado!,você deverá pagar {:.2f} de prestação.)".format(mensalidade))