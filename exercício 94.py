def leiaint(numero):
    num = input("Digite um número: ")
    while True:
        if num.isnumeric():
            print("Este é um número inteiro.")
            num = int(num)
            break
        else:
            print("Digite APENAS UM NÚMERO INTEIRO!")
            num = input("Digite um número: ")

x = leiaint('digite um número: ')
print(x)