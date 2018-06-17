import random


# funkcja

def srednia(lista):
    suma=0
    licznik = 0
    for n in lista:
        suma = suma + n
        licznik += 1
    wynik = suma / licznik
    return wynik





lista = []

for i in range(random.randrange(1, 7)):
    lista.append(random.randrange(1, 11))
print(lista)
print(srednia(lista))

