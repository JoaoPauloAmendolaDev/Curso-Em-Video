from random import randint
x1 = randint(0, 10)
x2 = randint(0, 10)
x3 = randint(0, 10)
x4 = randint(0, 10)
x5 = randint(0, 10)
z = (x1, x2, x3, x4, x5)
print("Os valores sorteados foram: {}".format(z))
z = sorted(z)
print("O menor valor sorteado foi {}\n"
      "O maior valor sorteado foi {}".format(z[0], z[-1]))

