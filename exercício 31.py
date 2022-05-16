nota = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota + nota2) / 2
if media < 5:
    print("Você foi reprovado, sua média foi {:.1f}.").format(media)
elif 5 <= media <= 6.9:
    print("Você está em recuperação, sua média foi {:.1f}.".format(media))
else:
    print("Parabéns, você foi aprovado, sua média foi {:.1f}".format(media))