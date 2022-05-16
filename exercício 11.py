nome = input("Digite o seu nome completo: ").strip()
nomeM = nome.upper()
nomem = nome.lower()
nomesplit = nome.split()
nomecontagem = len(nome)-nome.count(" ")


print ("Seu nome é: {}, Seu nome em maísculo é: {}, Seu nome em minusculo é: {}".format(nome, nomeM, nomem))
print("Seu primeiro nome é :",nomesplit[0])
print("Seu nome tem {} letras".format(nomecontagem))
