liczba = 1
suma = 0
while liczba < 1000:
    if liczba %3 ==0 or liczba %5 ==0:
        suma += liczba
        print(liczba, suma)
    liczba += 1