listapar = []
listaimpar = []
lista = []
x = 0
while True:
    x = (int(input("Digite o valor que deseja adicionar a lista: ")))
    if x % 2 == 0:
        listapar.append(x)
    elif x % 2 != 0:
        listaimpar.append(x)
    lista.append(x)
    resposta = input("DESEJA PARAR? [S/N]: ").lower().strip()[0]
    if resposta == 's':
        break
print(f'A primeira lista recebe todos os valores que são: {lista}\n'
      f'A segunda lista recebe apenas os valores pares: {listapar}\n'
      f'A terceira lista recebe apenas os valores ímpares: {listaimpar}')
