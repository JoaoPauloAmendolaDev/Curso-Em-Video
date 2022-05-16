soma = 0
for x in range(0, 6):
    n = int(input("digite um valor inteiro: "))
    if n % 2 == 0:
        soma = soma + n
print("O valor total somado é: {}".format(soma))
