sklep = {
    "1": ['Banany', 3.50, 10],
    "2": ['Ananas', 2.99, 5],
    "3": ['Papaja', 9.99, 1]
}
historia = []
while True:
    print("wpisz ID produktu: ")
    id_produktu = (input())
    if id_produktu not in sklep:
        print("Nie mamy tego produktu :( ")
        continue
    print("wpisz ilość: ")
    ilość = float(input())
    if ilość <=0:
        print("Wprowadziłeś liczbę niedodatnią. Zmieniam na dodatnią")
        ilość = abs(ilość)
    ile_mamy_na_stanie = sklep[id_produktu][2]
    if ilość <= ile_mamy_na_stanie:
        print("Damy radę")
        kwota = ilość * sklep[id_produktu][1]
        print("Za %s x%s zapłacisz %.2f" % (sklep[id_produktu][0], ilość, kwota))
        sklep[id_produktu][2] -=ilość
        historia.append((sklep[id_produktu][0], ilość, kwota))
    else:
        print("Nie damy rady :(")
    print("Czy chcesz jeszcze coś kupić")
    odpowiedź = input()
    if odpowiedź == "tak":
        print("NO TO KUPUJ!")
    else:
        break
suma =0
for nazwa, ilość, kwota in historia:
    print("%s, ilość: %s, cena: %.2f" % (nazwa, ilość, kwota))
    suma +=kwota
print("Za całe zakupy - do zapłaty %.2f zł." % suma)

# print(sklep[id_produktu])
# print(ilość, ile_mamy_na_stanie)