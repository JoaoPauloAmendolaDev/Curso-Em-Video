total = contador1000 = mbarato = Nmbarato = contador = 0
while True:
    nome = input("Digite o nome do produto: ")
    compra = float(input("Digite o valor do produto: "))
    total += compra
    if compra > 1000:
        contador1000 += 1
    contador += 1
    if contador == 1 or compra < mbarato:
        Nmbarato = nome
        mbarato = compra

    parar = ' '
    while parar not in 'SN':
        parar = str(input("Digite se você deseja parar [S/N]: ")).upper().strip()
    if parar in "S":
        print("O valor total gasto foi R$ {:.2f}\n"
              "Temos um total de {:.2f} produtos acima de R$ 999.99\n"
              "O produto mais barato foi {} que custa R$ {:.2f}".format(total, contador1000, Nmbarato, mbarato))
