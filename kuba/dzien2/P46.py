lista = [1,2,3,4,5,6,7,8,9]
tekst = input("Wpisz liczbę szukaną w zbiorze: ")


if tekst.isdigit():
    if int(tekst) in lista:
        print ("Liczba w zbiorze")
    else:
        print("Brak liczby w zbiorze")
else:
    print("Wpisz liczbę ! ")



if tekst in lista:
    print ("Liczba zawarta w zbiorze")
elif tekst.isdigit():
    print ("Brak liczby w zbiorze")
elif:
    print ("Wpisz liczbę ! ")

