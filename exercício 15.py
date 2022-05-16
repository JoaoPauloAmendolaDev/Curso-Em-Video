texto = input("Digite um texto caralho: ").lower().strip()
print("A letra A aparece : {} vezes no texto".format(texto.count("a")))
print("A primeira letra A aparece na posição: {}".format(texto.find("a")+1))
print("A ultima letra A aparece na posição: {}".format(texto.rfind("a")+1))

