lista1 = []
lista2 = []
contadorPessoas = maiorpeso = menorpeso = nomemenorpeso = nomemaiorpeso = 0
while True:
    lista2.append(str(input("Digite um nome: ")))
    lista2.append(float(input("Digite o peso: ")))
    if contadorPessoas == 0:
        maiorpeso = menorpeso = lista2[1]
    else:
        if lista2[1] > maiorpeso:
            maiorpeso = lista2[1]
        if lista2[1] < menorpeso:
            menorpeso = lista2[1]
    contadorPessoas += 1
    lista1.append(lista2[:])
    lista2.clear()
    continuar = input("Deseja continuar? [S/N]: ").lower().strip()[0]
    if continuar == 'n':
        break
print(f'O maior peso foi de {maiorpeso}Kg', end='')
print('Peso de: ', end='')
for num in lista1:
    if num[1] == maiorpeso:
        maiorpeso = num[1]
        print(f'[{num[0]}]', end=' ')
print(f'O menor peso foi de {menorpeso}Kg ', end='')
for p in lista1:
    if p[1] == menorpeso:
        menorpeso = p[1]
        print(f'[{p[0]}]', end=' ')
