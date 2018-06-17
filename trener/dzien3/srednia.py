import random

def srednia(lista):
    if lista == []:
        return 0
    suma = 0
    licznik = 0
    for n in lista:
        suma += n
        licznik += 1
    wynik = suma / licznik
    return wynik

lista = []

for i in range(random.randrange(1, 7)):
    lista.append(random.randrange(1, 11))
print(lista)

print(srednia(lista))
print(srednia([]))

print("tutaj skończyliśmy pracę nad naszą listą do testów")