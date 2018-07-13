# ćwiczenia pro5
import random

def srednia (lista):
    if lista == []:
        return 0
    suma = 0
    licznik = 0
    for n in lista:
        suma += n
        licznik += 1
    return round(suma / licznik, 3)


lis = []
for i in range(random.randrange(1, 7)):
    lis.append(random.randint(1, 11))
print(lis)
print([])
print(srednia([]))
print(srednia(lis))
print('koniec')