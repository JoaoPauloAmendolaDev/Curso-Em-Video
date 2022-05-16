tupla = ('banana','maça','pera','frutas','uva','melancia','suco','vitamina')
for x in tupla:
    contador = tupla.count('aeiou')
    print(f"\nNa palavra {x} temos => ",end='')
    for letra in x:
        if letra.lower() in "aeiou":
            print((letra), end=' ')