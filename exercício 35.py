valor = float(input("Digite o valor do produto: "))
FDP = int(input("Digite 1 para pagar à vista/cheque. \n"
                "Digite 2 para pagar à vista no cartão. \n"
                "Digite 3 para pagar em até 2x no cartão. \n"
                "Digite 4 para pagar em 3x ou mais. \n"
                "Digite aqui a opção selecionada : "))
if FDP == 1:
    valordescontado = valor - (valor * 0.1)
    print("O valor é {:.2f} reais, "
          "mas com desconto fica {:.2f} reais".format(valor, valordescontado))
elif FDP == 2:
    valordescontado = valor - (valor * 0.05)
    print("O valor é {:.2f} reais, "
          "mas com desconto fica {:.2f} reais".format(valor, valordescontado))
elif FDP == 3 or FDP == 4:
    parcelas = int(input("Digite o número de parcelas: "))
    if parcelas <= 2:
        QDP = valor / parcelas
        print("O valor é {:.2f} reais.\n Não há desconto e"
              "cada parcela custará {} reais.".format(valor, QDP))
    if parcelas > 2:
        valorsomado = valor + (valor * 0.2)
        QDP = valorsomado / parcelas
        print("O valor é {:.2f}, entretanto, "
              "com juros do cartão ele fica {:.2f} reais\n"
              "sua compra será parcelada em {} parcelas de {:.2f} reais COM JUROS"
              ".".format(valor, valorsomado, parcelas, QDP))
else:
    print("Digite um valor válido.")
