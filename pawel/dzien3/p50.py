sklep ={
    "1":["Arbuz", 3.50, 10],
    "2":["Banan",2.99,5 ],
    "3":["Cebula",9.99,1]
}


historia = []
while True:
    print("Wpisz ID produktu")
    id_produktu=input()
    if id_produktu not in sklep:
        print("NIe ma takiego produktu")
        continue

    print("Wpisz ilość")
    ilość = float(input())
    if ilość <=0 :
        print("Wprowadziłeś ilość ujemną. Zamieniam na dodatnią")
        ilość = abs(ilość)
    ile_mamy_na_stanie = sklep[id_produktu][2]
    if ilość<= ile_mamy_na_stanie:
         print("Damy radę")
         kwota= ilość*sklep[id_produktu][1]
         print("Za %s x %s zapłacisz %.2f " %(sklep[id_produktu][0], ilość, kwota))

         sklep[id_produktu][2]-=ilość
         historia.append((sklep[id_produktu][0], ilość, kwota))

    else:
         print("Nie damy rady")
    print("Czy chcesz jeszcze coś kupić?")
    odpowiedź = input()
    if odpowiedź == "tak":
        print("no to kupuj")
    else:
        break
# print(sklep[id_produktu])
# print(ilość)
# print(ile_mamy_na_stanie)
#print("Zapłacisz łącznie: %.2f " )
print(historia)
suma=0
for nazwa, ilość, kwota in historia:
    print ("%s, ilość: %s, cena: %.2f" %(nazwa, ilość, kwota))
    suma+=kwota
print("Za całe zakupy do zapłaty %.2f zł." %suma)