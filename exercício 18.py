V = int(input("Digite a velocidade que o carro estava: "))
multa = 0
if V >= 81:
    multa = 7 * (V - 80)
    print("Você foi multado em {} reais, ande com mais cautela.".format(multa))
else:
    print("Você está dentro do limite, parabéns!")