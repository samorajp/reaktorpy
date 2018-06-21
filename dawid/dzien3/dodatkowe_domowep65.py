# p65 Zadanie

import random

def srednia(lista):
    if lista == []:
        return 0
    sum = 0
    licznik1 = -1000
    licznik2 = 1000

    for n in lista:
        licznik1 += 1
    wynik = licznik1 / licznik2
    return wynik

print("Elementy losowo z zakresu od [-1000 do 1000]: ")
lista = []
lista.append(random.randrange(-1000, 1000))
print(lista)

