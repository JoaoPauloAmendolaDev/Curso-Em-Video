def notas(*num, sit=False):
    maior = menor = media = soma = contador = 0
    dicionario = {}
    dicionario['Maior'] = (max(num))
    dicionario['Menor'] = (min(num))
    dicionario['Media'] = sum(num) / len(num)
    dicionario['Quantidade'] = len(num)
    if sit:
        if dicionario['Media'] > 6:
            dicionario['Situação'] = "BOA"
        if 4 < dicionario['Media'] < 6:
            dicionario['Situação'] = "MÉDIA"
        if dicionario['Media'] < 4:
            dicionario['Situação'] = "RUIM"
    print(dicionario)
    return dicionario


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
