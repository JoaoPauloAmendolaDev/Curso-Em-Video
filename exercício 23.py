n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 > n3:
    print("{} é o maior número, enquanto {} é o menor.".format(n1, n3))
if n1 > n3 > n2:
    print("{} é o maior número, enquanto {} é o menor.".format(n1, n2))
if n2 > n1 > n3:
    print("{} é o maior número, enquanto {} é o menor.".format(n2, n3))
if n2 > n3 > n1:
    print("{} é o maior número, enquanto {} é o menor.".format(n2, n1))
if n3 > n1 > n2:
    print("{} é o maior número, enquanto {} é o menor.".format(n3, n2))
if n3 > n2 > n1:
    print("{} é o maior número, enquanto {} é o menor.".format(n3, n1))
else:
    print("Não pode colocar números iguais.")
#outra possibilidade mais simples é transformar os 3 números em uma lista!
#lista = [n1, n2, n3]
#para organizar a lista em ordem númerica, usamos lista_ordenada = sort(lista)
#print("O menor valor é {}".format(lista_ordenada[0]) (isso pega o maior número na lista)
#print("O maior valor é {}".format(lista_ordenada[2]) (assim, pegamos o menor da lista)