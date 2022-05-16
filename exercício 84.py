lista_mulheres = []
lista = []
lista_idade_acima_media = []
dic = {}
soma = media_de_idade = contador_pessoas = 0
while True:
    contador_pessoas += 1
    dic["Nome"] = str(input("Nome: "))
    dic["idade"] = int(input("Idade: "))
    dic["Sexo"] = str(input("Sexo: [H/M] ")).lower().strip()[0]
    soma += dic["idade"]
    if dic["Sexo"] == "m":
        lista_mulheres.append(dic['Nome'])
    lista.append(dic.copy())
    parar = str(input("Parar? [S/N] ")).lower().strip()[0]
    if parar == 's':
        break
media_de_idade = soma / contador_pessoas
for x in lista:
    for k, v in x.items():
        if k == "idade":
            if v > media_de_idade:
                lista_idade_acima_media.append(x.get("Nome"))
print(f'A quantidade de pessoas cadastradas foram: {contador_pessoas}')
print(dic)
print(f'A lista de mulheres é: {lista_mulheres}')
print(f'A média de idade dessas pessoas foi: {media_de_idade:.0f} anos.')
print(f'A lista de pessoas com idade acima da média é: {lista_idade_acima_media}')
