times = ('Santos','ATMG','Cortinas','Cuiaba','Inter','Chapecoense','Bragantino','Palmeiras','Flamengo','Coritiba','SP','Botafogo','Fluminense','AmericaMG','Ceara','ATPR','ATGO','Goias','Juventude','Fortaleza')
print("Os 5 primeiros colocados são :{}\n"
      "Os 4 últimos colocados são: {}\n"
      "A Chapecoense está em: {} colocado.\n"
      "A Ordem Alfabética dos times é: {}\n"
      "".format(times[:5], times[-4:], times.index('Chapecoense') + 1, sorted(times)))
