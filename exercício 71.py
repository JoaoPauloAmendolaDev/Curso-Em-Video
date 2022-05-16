lista = []
contador = 0
for x in range(0, 5):
    n = int(input("Digite um valor: "))
    pos = 0
    if contador == 0 or n > lista[-1]:
        lista.append(n)
    else:
        while True:
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    contador += 1
    print(lista)
