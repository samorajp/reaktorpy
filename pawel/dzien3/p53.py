licznik = 3
suma = 0
suma1=0
while True:
    kwadrat = licznik ** 2
    suma = suma + kwadrat
    suma1 = suma1 + licznik
    print(licznik, licznik**2,suma1, suma)
    licznik +=1


    if licznik > 9:
        break
    