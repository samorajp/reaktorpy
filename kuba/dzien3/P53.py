licznik = 3
suma = 0
while True:
    print(licznik,licznik**2)
    kwadrat = licznik ** 2
    suma = suma + kwadrat
    print(suma)
    licznik+=1
    if licznik==10:
        break

