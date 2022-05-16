contador = continuar = 0
var1 = []
while True:
    if continuar == 's' or continuar == 0:
        var1.append(int(input('Digite um valor: ')))
        var1.sort(reverse=True)
    if continuar == 'n':
        break
    contador += 1
    continuar = input('Deseja continuar? [S/N]: ').lower().strip()[0]

print(f'Foram {contador} números digitados.')
try:
    print(f'{var1.index(5)} 5 Foi encontrado!')
except:
    print("Não há número 5 na lista.")
print(f'A ordem dos números reversa é: {var1}')
