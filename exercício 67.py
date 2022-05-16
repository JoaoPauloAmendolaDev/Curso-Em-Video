x = ('banana', 3
     , 'maçã', 2.5
     , 'pera', 5
     , 'alface', 1.99
     , 'notebook', 2999.99)
print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS!":^40}')
print("-" * 40)
"""for pos in range(0, len(x)):
    if pos % 2 == 0:
        print("{:.<30}".format(x[pos], end=''))
    else:
        print("R${:>8.2f}".format(x[pos]))"""
for pos in range(0, len(x)):
    if pos % 2 == 0:
        print(f'{x[pos]:.<30}', end="")
    else:
        print(f'R${x[pos]:>7.2f}')