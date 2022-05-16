contadorcondicional = contadorlista = contador1 = contador2 = soma = somac3 = maior = 0
lista = [[], [], [], [], [], [], [], [], []]
while True:
    for z in range(0, 9, 1):
        numero = int(input(f"Digite um número para [{contador1, contador2}] : "))
        if contador2 < 2:
            contador2 += 1
        elif contador2 == 2:
            contador2 = 0
            contador1 += 1
        lista[contadorlista].append(numero)
        contadorlista += 1
        if numero % 2 == 0:
            soma += numero
    '''if lista[4] >= lista[3] and lista[4] >= lista[5]:
        maior = lista[4]
    if lista[3] >= lista[4] and lista[3] >= lista[5]:
        maior = lista[3]
    if lista[5] >= lista[4] and lista[5] >= lista[3]:
        maior = lista[5]'''
    for num in lista[3:6]: #Esse método é mais prático que 3 if's juntos.
        maior = lista[3]
        if num >= maior:
            maior = num

    somac3 = lista[2] + lista[5] + lista[8]
    print(f'{ lista[0] } { lista[1] } { lista[2] }\n'
          f'{ lista[3] } { lista[4] } { lista[5] }\n'
          f'{ lista[6] } { lista[7] } { lista[8] }\n'
          f'O maior número da segunda linha é: {maior}\n'
          f'Todos os valores pares somados dão: {soma}\n'
          f'A soma dos 3 dígitos da terceira coluna são: {somac3}')
    if contadorcondicional == 0:
        break
