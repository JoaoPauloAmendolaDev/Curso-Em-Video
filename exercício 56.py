maior = menor = media = contador = soma = 0
contador2 = 1
while contador2 > 0:
    x = int(input("Digite um número: "))
    z = input("Deseja continuar? [S/N]").upper().strip()
    contador += 1
    if contador == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
    if z == "N":
        contador2 = 0
    soma += x
media = soma / contador
print("O maior número é {}\n"
      "O menor número é {}\n"
      "A média entre todos os digitados é {}\n"
      "Você digitou {} números".format(maior, menor, media, contador))
