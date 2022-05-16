salario = float(input("Digite o valor que deseja para o aumento:" ))
if salario > 1250:
    novosalario = ((salario * 0.10) + salario)
else:
    novosalario = ((salario * 0.15) + salario)
print("Parabéns, seu salário aumentou para: {:.2f}".format(novosalario))