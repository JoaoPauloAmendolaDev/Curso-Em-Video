ficha = []

while True:
    nome = str(input("Nome: "))
    n1 = float(input("nota 1: "))
    n2 = float(input("nota 2: "))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resposta = input("Deseja continuar?: [S/N] ").strip().lower()[0]
    if 'n' in resposta:
        break
print(f'''{'Numero':<4} {'Nome':>10} {"Média":>10}''')
print('-'* 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:>13}{a[2]:>10.1f}')
while True:
    print('-'*26)
    opc = int(input("Mostrar notas de qual aluno? [999 para sair] "))
    x = len(ficha)
    if opc == 999:
        break
    if opc <= x - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print("Programa finalizado.")

