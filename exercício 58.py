while True:
    n = int(input("Digite um número para sua tabuada (Digite um negativo para parar): "))
    if n < 1:
        print("Operação Terminada.")
        break
    for x in range(0, 11):
        resultado = n * x
        print("{} * {} = {} ".format(n, x, resultado))
