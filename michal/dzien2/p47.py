lista = (1, -2)

if lista[0] < 0 and lista[1] < 0:
    print('ujemne')
elif lista[0] < 0:
    print('pierwsza ujemna')
elif lista[1] < 0:
    print('druga ujemna')
else :
    print('dodatnie')