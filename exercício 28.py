n = int(input("para converter para \n"
              "binário digite [1], \n"
              "para octal, digite [2],\n"
              "para hexadecimal, digite [3]\n"
              "Digite agora: "))
if n == 1:
    x = int(input("digite o valor que deseja converter para binário: "))
    print("O valor foi convertido para: {:b}".format(x))
elif n == 2:
    x = int(input("Digite o valor que deseja converter para octadecimal: "))
    print("O valor foi convertido para: {:o} .".format(x))
elif n == 3:
    x = int(input("Digite o valor que deseja converter para hexadecimal: "))
    print("O valor foi convertido para: {:X}".format(x))
else:
    print("Digite um valor válido.")
