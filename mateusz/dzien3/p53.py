licznik = 3


sumaA = 0
sumaB = 0

while licznik < 10:
    #print (licznik)
    kwadrat = licznik*licznik
    suma= licznik+kwadrat
    print(str(licznik) + ', '  + str(kwadrat) + ', suma to '+ str(suma))
    licznik = licznik+1
    sumaA = sumaA+licznik-1
    sumaB = sumaB+kwadrat
    print('suma liczb to: ' + str(sumaA) + ', a suma kwadratów to: ' + str(sumaB))


