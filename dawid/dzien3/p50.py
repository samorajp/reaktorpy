# p50 zadanie
sklep = {
    1: ['Arbus', 3.50, 10],
    2: ['Banan', 2.99, 5],
    3: ['Cebula', 9.99, 1],
}

sum = 0
historia = []
while True:
    print("Wpisz ID produktu: ")
    id_produktu = int(input())

    if id_produktu not in sklep:
        print("Nie ma produktu")
        continue

    print("Wpisz ilosc")
    ilosc = int(input())
    if ilosc <= 0:
        print("Wprowadziłesz wartosc niedodatna. Zamieniam na dodatnia.")
        ilosc = abs(ilosc)

    ile_mamy_na_stanie = sklep[id_produktu][2]
    if ilosc <= ile_mamy_na_stanie:
        print("Damy rade: ")
        kwota = ilosc * sklep[id_produktu][1]
        print("Za %s x%s zapłacisz %s" % (sklep[id_produktu][0], ilosc, kwota))
        suma += kwota
        sklep[id_produktu][2] -= ilosc
        historia.append((sklep[id_produktu][0], ilosc, kwota))
    else:
        print("Nie damy rade")

    odpowiedz = print("Czy chcesz jeszcze cos kupic?")
    odpowiedz = input()

    if odpowiedz == "tak":
        print("No to kupuj!")
    else:
        break

    print(historia)
    print("Za całe zakupy: %.2f" % suma)

