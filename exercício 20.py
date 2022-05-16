distancia = int(input("Digite a distância da viagem em KM: "))
viagem1 = distancia * 0.5
viagem2 = distancia * 0.45
if distancia <= 200:
    print("O valor da sua viagem será {:.2f} reais.".format(viagem1))
else:
    print("O valor da sua viagem será {:.2f} reais.".format(viagem2))
