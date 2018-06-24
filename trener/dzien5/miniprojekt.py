import pymysql

conn = pymysql.connect("localhost", "root", "asddsa", "projekt_python")
c = conn.cursor()

def ekran_logowania():
    c.execute("select * from logowanie")
    uzytkownicy = c.fetchall()

    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")

    for uzytkownik in uzytkownicy:
        login_w_bazie = uzytkownik[0]
        haslo_w_bazie = uzytkownik[1]
        typ_konta = uzytkownik[2]

        if login_w_bazie == login and haslo_w_bazie == haslo:
            print("SUPER")
            if typ_konta == "A":
                print("Witaj administratorze")
            else:
                print("Witaj użytkowniku")
            return login, typ_konta

    # użytkownik wpisał złe dane
    # bo return nigdy nie nastąpił
    return None, None


def ekran_logowania_do_skutku():
    while True:
        login, typ_konta = ekran_logowania()
        if login != None:
            return login, typ_konta
        else:
            print("Próba nieudana")



def wyloguj_sie():
    print("Wylogowano")
    exit()

def zobacz_oferte():
    print()
    print("### Pokazuje ofertę  ###")
    c.execute("select * from produkty")
    oferta = c.fetchall()


    for produkt in oferta:
        print("%3s %10s  %5s" % (produkt[0], produkt[1], produkt[2]))
    print()

def zloz_zamowienie(login):
    print("Składamy zamówienie")

    kod = input("Podaj kod zamówienia: ")

    while True:
        zobacz_oferte()
        kod_produktu = input("Wprowadź kod produktu:")
        ilosc = input("Podaj ilość: ")

        zapytanie = """
            insert into zamowienia (login, kod_zamowienia, id_produktu, ilosc)
            values (%s, %s, %s, %s)
        """

        c.execute(zapytanie, (login, kod, kod_produktu, ilosc))
        conn.commit()

        odp = input("Czy chcesz dalej kupować? [tak/nie]")

        if odp != "tak":
            break

    print("Zamównienie o kodzie %s zostało złożone" % kod)

def historia_zamowien(login):
    print("Historia zamówień poniżej.")

    zapytanie = """
        select zamowienia.kod_zamowienia, 
        produkty.nazwa, zamowienia.ilosc, produkty.cena
        from zamowienia, produkty
        where login = %s and 
        zamowienia.id_produktu = produkty.id_produktu
    """

    c.execute(zapytanie, login)
    pozycje = c.fetchall()

    for pozycja in pozycje:
        print(pozycja)

def dodaj_produkt():
    nazwa = input("Podaj nazwę nowego produktu: ")
    cena = input("Podaj cenę nowego produktu: ")

    zapytanie = """
        insert into produkty (nazwa, cena) values (%s, %s)
    """

    c.execute(zapytanie, (nazwa, cena))
    conn.commit()

    print("Pomyślnie dodano produkt: %s" % nazwa)




def menu(login, typ_konta):
    if typ_konta == "U":
        print("## MENU, witaj %s ##" % login)
        print("1 - Wyloguj się")
        print("2 - Zobacz ofertę")
        print("3 - Złóż zamówienie")
        print("4 - Historia zamówień")
        print("5 - D")

        akcja = input("Co chcesz zrobić? ")

        if akcja == "1":
            wyloguj_sie()
        elif akcja == "2":
            zobacz_oferte()
        elif akcja == "3":
            zloz_zamowienie(login)
        elif akcja == "4":
            historia_zamowien(login)
        else:
            print("Nie wiem o co Ci chodzi.")
        menu(login, typ_konta)
    elif typ_konta == "A":
        print("1 - Wyloguj")
        print("2 - Dodaj produkt")
        print("3 - ...")
        print("4 - ...")

        akcja = input("Co chcesz zrobić? ")

        if akcja == "1":
            wyloguj_sie()
        elif akcja == "2":
            dodaj_produkt()
        else:
            print("Nie wiem o co Ci chodzi.")
        menu(login, typ_konta)




login, typ_konta = ekran_logowania_do_skutku()


menu(login, typ_konta)