frase = input("Digite uma frase: ").strip().lower()
palavras = frase.split()
juntar = "".join(palavras)
fraseinvertida = juntar[::-1]
if juntar == fraseinvertida:
    print("Você digitou {}\n"
          "E o seu contrário é {}\n"
          "O que o torna um PALINDROMO!".format(frase, fraseinvertida))
else:
    print("Você digitou {}\n"
          "E o seu contrário é {}\n"
          "O que o não torna um PALINDROMO!".format(frase, fraseinvertida))

