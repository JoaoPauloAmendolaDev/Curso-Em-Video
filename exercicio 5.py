dias = int(input("Diga por quantos dias o carro foi utilizado: "))
km = float(input("Diga por quantos KM esse carro foi utilizado: "))
valordia = dias * 60
valorkm = km * 0.15
valortotal = valorkm + valordia
print("Você deverá pagar {:.2f} Reais pela utilização de nosso carro, obrigado.".format(valortotal))
