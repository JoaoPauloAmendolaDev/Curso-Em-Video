def fatorial(a, b=False):
    if not b:
        for c in range(a, 0, -1):
            a *= c
        return a
    if b:
        print(a, end=' => ')
        for c in range(a - 1, 0, -1):
            a *= c
            print(a, end=' => ')
        print("FIM")


num = int(input("Digite o valor: "))
apresentar = input("Deseja apresentar o processo na tela? "
                   "se não, será apresentado apenas o resultado: [SIM/NÃO]"
                   ).strip().lower()[0]
while True:
    if apresentar not in "sn":
        print("Digite SIM ou NÃO.")
        apresentar = input("Deseja apresentar o processo na tela? "
                           "se não, será apresentado apenas o resultado: [SIM/NÃO] "
                           ).strip().lower()
    else:
        break
if apresentar == "s":
    resultado = fatorial(num, True)
else:
    resultado = fatorial(num)
    print(f'O resultado fatorial de {num} é {resultado}.')



