import datetime


def voto(ano):
    ano_atual = datetime.date.today().year
    global idade
    idade = ano_atual - ano
    if 16 <= idade < 18 or idade > 65:
        return "VOTO OPCIONAL"
    elif idade < 16:
        return "VOTO NEGADO"
    elif 18 <= idade < 65:
        return "VOTO OBRIGATÓRIO"


nascimento = int(input("Digite o ano de nascimento: "))
idade = 0
resultado = voto(nascimento)
print(f'Você tem {idade} anos e seu resultado é {resultado}')
