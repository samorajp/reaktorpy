#imie nazwisko grupa
#przechowywac dane w pliku lista_stu.txt
#dodawanie - usuwanie - pokazanie listy
#usuwanie o nazwisku
#menu interaktywne

def dodaj():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    grupa = int(input("Podaj grupę: "))

    plik = open("lista_stu.txt", "a")
    plik.write("%s,%s,%i\n" % (imie, nazwisko, grupa))
    plik.close()
    print("dodane")

def poka():
    plik = open("lista_stu.txt", "r")
    for line in plik:
        print(line, end='')
    plik.close()
    print("\n")


def usun():
    nazwisko = input("podaj nazwisko studenta\n")
    plik = open("lista_stu.txt", "r")
    zm = ""
    jest = False
    for i in plik:
        dane = (i.strip().split(','))
        if dane[1] != nazwisko:
            zm += i
        else:
            jest = True
    print("brak studenta z nazwiskiem - %s -\n" % (nazwisko))

    plik.close()

    plik = open("lista_stu.txt", "w")
    plik.write(zm)
    plik.close()


while (True):
    dec = input("D odaj | U suń | P okaż liste | W yjdź\n")

    if (dec == "D" or dec == "d"):
        dodaj()

    elif (dec == "U" or dec == "u"):
        usun()

    elif (dec == "P" or dec == "p"):
        poka()
    elif (dec == "W" or dec == "w"):
        print("dziekuję za uwagę")
        break
