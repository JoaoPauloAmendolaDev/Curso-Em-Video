'''listapar = []
listaimpar = []
lista = []
for x in range(0, 7):
    z = int(input("Digite um valor: "))
    if z % 2 == 0:
        listapar.append(z)
    elif z % 2 != 0:
        listaimpar.append(z)
    lista.append(z)
    listapar.sort()
    listaimpar.sort()
print(f'Os valores inseridos foram:{lista}\n'
      f'Os valores inseridos IMPARES foram: {listaimpar}\n'
      f'Os valores inseridos PARES foram: {listapar}')'''

lista = [[], []]
contador = 0
while True:
    num = int(input("Digite o valor necessário: "))
    if num % 2 == 0:
        lista[0].append(num)
    if num % 2 != 0:
        lista[1].append(num)
    lista[0].sort()
    lista[1].sort()
    contador += 1
    if contador == 7:
        break
print(f'{lista[0]} é a lista PAR!\n'
    f'{lista[1]} é a lista IMPAR!')
