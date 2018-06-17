liczba = 3
suma = 0

while liczba < 10:
    kwadrat = liczba * liczba
    print('kwadrat liczby ' + str(liczba) + " to " + str(kwadrat))
    liczba += 1
    suma += kwadrat
    pass
print("\n")
print('suma wszystkich kwadratów to: ' + str(suma))

