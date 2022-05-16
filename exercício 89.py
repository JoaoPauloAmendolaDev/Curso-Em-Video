def maior(*num):
    x = []
    contador = maior_numero = 0
    while True:
        valor = (int(input("Digite um valor:")))
        if contador == 0:
            maior_numero = valor
        if valor > maior_numero:
            maior_numero = valor
        x.append(valor)
        pergunta = str(input("Deseja parar? [S/N] ")).upper().strip()[0]
        while pergunta not in "SN":
            print("Digite apenas sim ou não!")
            pergunta = str(input("Deseja parar? [S/N] ")).upper().strip()[0]
        print(x)
        print(maior_numero)
        print(len(x))
        contador += 1
        if pergunta == 'S':
            break
#Esse daqui você coloca os valores DENTRO da def

def maior2(*num):
    maior = valor
    print('=-'*30)
    print("Analisando valores passados...")
    for x in num:
        for contador_lista, numero_lista in enumerate(x):
            print(f'{numero_lista}',end=' ')
            if contador_lista + 1 == len(x):
                print(f'foram informados {len(x)} valores ao todo')
                print(f'O maior número informado foi o {maior}')
            if numero_lista > maior:
                maior = numero_lista

    print('=-' * 30)
#Esse daqui você coloca os valores por FORA da def








contador = 0
lista = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    pergunta = str(input("Deseja parar? [S/N] ")).upper().strip()[0]
    while pergunta not in "SN":
        print("Digite apenas sim ou não!")
        pergunta = str(input("Deseja parar? [S/N] ")).upper().strip()[0]
    else:
        if pergunta == 'S':
            break
    contador += 1
maior2(lista)




