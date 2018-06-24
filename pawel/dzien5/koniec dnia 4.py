import pymysql

conn = pymysql.connect("localhost", "root", "03041983pawel", "projekt_python")

c = conn.cursor()

def wyloguj_się():
    print("Wylogowano")
    exit()
def zobacz_oferte():
    print ("Zobaczam ofertę ")
    c.execute("select * from produkty")
    oferta = c.fetchall()
    for produkt in oferta:

        print("%s ---- %s , %s" % produkt)
def zloz_zamowienie():
    print("Składamy zamówienie")

def historia_zamowien():
    print("Historia zamówień poniżej.")

def menu():
    print("1 - Wyloguj się")
    print("2 - Zobacz ofertę")
    print("3 - Złóż zamówienie")
    print("4 - Historia zamówień")
    akcja = input("Co chcesz zrobić? ")

    if akcja == "1":
        wyloguj_się()
    elif akcja == "2":
        zobacz_oferte()
    elif akcja == "3":
        zloz_zamowienie()
    elif akcja == "4":
        historia_zamowien()
    else:
        print("Nie wiem o co Ci chodzi.")
    menu()

menu()

exit()











conn = pymysql.connect("localhost", "root", "03041983pawel", "projekt_python")

c = conn.cursor()
c.execute("select * from logowanie")
    # print(c.fetchall())
uzytkownicy = c.fetchall()

def ekran_logowania():

    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")
    for uzytkownik in uzytkownicy:
        login_w_bazie = uzytkownik[0]
        haslo_w_bazie = uzytkownik[1]
        typ_konta_w_bazie = uzytkownik[2]
        if login_w_bazie == login and haslo_w_bazie == haslo:
            print("Super")
            if typ_konta_w_bazie == "A":
                print("Witaj Adminie")
            else:
                print ("Witaj szary użytkowniku")
            return login, typ_konta_w_bazie
    #uytkownik wpisał złe dane bo return nigdy nie nastąpił
    return None, None

def ekran_logowania_do_skutku():
    while True:
       login, typ_konta = ekran_logowania()
       if login != None:
        return login, typ_konta
       else:
            print("Nieudane logowanie")

#print(ekran_logowania() ) #login,typ_konta



zalogowany_user, typ_konta = ekran_logowania_do_skutku()


#c.execute("insert into logowanie values ('ddd', 'ddd123', 'U');")

if typ_konta == "A":

    podany_login = input("Podaj login nowego użytkownika: ")
    podane_haslo = input("Haslo dla nowego uzytkownika: ")


    c.execute("insert into logowanie values (%s, %s, %s)", (podany_login, podane_haslo, "U"))
    conn.commit()
else:
    print("Nie jesteś administratorem, poproś dorosłego o pomoc")

