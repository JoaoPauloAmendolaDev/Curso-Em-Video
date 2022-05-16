numero = 0
numerodevezes = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        numero = numero + c
        numerodevezes = numerodevezes + 1
print(("A soma de todos os valores é {}, onde foram adicionados {} números.").format(numero, numerodevezes))

