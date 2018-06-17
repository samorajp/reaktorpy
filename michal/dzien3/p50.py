sklep = {
    1: ['Arbuz', 3.50, 10],
    2: ['Banan', 2.99, 5],
    3: ['Cytryny', 9.99, 1]
}

#suma = 0
hisoria = []

while True:
    print('aby zamówić wpisz ID produktu')
    id = int(input())
    if id not in sklep.keys():  # sklep.keys() == sklep - wyszukuje, po kluczach - pierwszej wartości
        print('brak produktu')
        continue
    ilosc = float(input('wpisz ilość zamawianego produktu\n'))
    if ilosc <= 0:
        print('ilość jest ujemna!!\n zmieniam na dodatnią')
    ilosc = abs(ilosc)
    print(ilosc)
#    produkt = sklep[id][0]
#    cena = sklep[id][1]
#    stan = sklep[id][2]
    produkt, cena, stan = sklep[id]

    if ilosc <= stan:
        print('możemy zrealizować')
        kwota = round(cena * ilosc, 2)
        print('zamowienie %s * %s .szt = %s' % (produkt, ilosc, kwota))
#        suma += kwota
        sklep[id][2] -= ilosc
        hisoria.append((id, produkt, ilosc, kwota))
    else:
        print('za duże zamówienie')
    #    ilosc = int('brakuje na magazynie. zmodyfikuj zamówienie')
    print('czy chcesz, zanabyć jakieś jeszcze dobra, Panie')
    odp = input()
    if odp == 'T':
        pass
    else:
        break

#print('suma za zaupy: %s' % suma)
print(hisoria)
i = 0
summa = 0
for id2, produkt2, ilosc2, kwota2 in hisoria:
    i +=1
    summa += kwota2
    print(i, produkt2, ilosc2, kwota2)
    print('suma za zakupy: %.2f' % summa)

#
#
# print('\n--------------'*3)
# print(sklep[id])
# print(ilosc)
# print('cena', cena)
# print(sklep[id][-1])