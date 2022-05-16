while True:
    x = input("Digite uma expressão: ")
    x1 = x.count('(')
    x2 = x.count(')')
    if x1 == x2:
        print('Sua expressão está correta.')
    else:
        print('Sua expressão está incorreta.')