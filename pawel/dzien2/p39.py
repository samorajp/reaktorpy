slownik={'jeden':1, 'dwa':2, 'dwójka':2, 'trzy':3, 'cztery':4, 'pięć':5}

napis = input("Wpisz napis: ")
print(napis)
print(slownik[napis])  #wpisując slownik[napis] --  slownik['dwojka'] daje nam 2 a my chcemy, zeby te  slowo dwojka bylo tym napisem, co wprowadzamy
#wpisanym akurat przez uzytkownika. najpiewr definiujemy zbior napisow i odpowiadajacych im wartosci i to zwaraca nam ta wartosc zapisanam, zdefiniowana jako odpowiadajaca napisowi,nazwie cyfry