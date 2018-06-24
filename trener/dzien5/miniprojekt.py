import pymysql

conn = pymysql.connect("localhost", "root", "asddsa", "projekt_python")
c = conn.cursor()

def ekran_logowania():
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
        print("%10s  %5s" % (produkt[1], produkt[2]))
    print()

def zloz_zamowienie():
    print("Składamy zamówienie")

def historia_zamowien():
    print("Historia zamówień poniżej.")

def menu():
    print("## MENU ##")
    print("1 - Wyloguj się")
    print("2 - Zobacz ofertę")
    print("3 - Złóż zamówienie")
    print("4 - Historia zamówień")

    akcja = input("Co chcesz zrobić? ")

    if akcja == "1":
        wyloguj_sie()
    elif akcja == "2":
        zobacz_oferte()
    elif akcja == "3":
        zloz_zamowienie()
    elif akcja == "4":
        historia_zamowien()
    else:
        print("Nie wiem o co Ci chodzi.")
    menu()



ekran_logowania_do_skutku()
menu()
exit()









c.execute("select * from logowanie")
uzytkownicy = c.fetchall()





zalogowany_user, typ_konta = ekran_logowania_do_skutku()

if typ_konta == "A":
    podany_login = input("Podaj login nowego użytkownika: ")
    podane_haslo = input("Hasło dla nowego użytkownika: ")

    c.execute("INSERT INTO logowanie VALUES (%s, %s, %s)", (podany_login, podane_haslo, 'U'))
    conn.commit()
else:
        pass