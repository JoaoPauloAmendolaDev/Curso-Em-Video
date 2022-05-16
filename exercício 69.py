n = []
posiçaomaior = posiçaomenor = maior = menor = contador = 0
for x in range(0, 5):
    n.append(int(input("Digite o valor que deseja: ")))
for pos, valor in enumerate(n):
    if pos == 0:
        menor = n[0]
    else:
        if valor < menor:
            menor = valor
            posiçaomenor = pos
        if valor > maior:
            maior = valor
            posiçaomaior = pos
    contador += 1
print(f'O total de valores digitados foram: {n}\n'
      f'O menor valor foi: {menor} na posição {posiçaomenor}\n'
      f'O maior valor foi: {maior} na posição {posiçaomaior}\n')

