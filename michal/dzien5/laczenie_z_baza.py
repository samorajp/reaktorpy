import pymysql

class Pracownicy():
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'C!ec666', 'python_testowy', charset='utf8')
        self.c = self.conn.cursor()
        print("połączonie ustanowione")
        self.menu()

    def insert(self):
        imie = input("imie: ")
        nazwisko = input("nazwisko: ")
        rokUrodzenia = input("rok urodzenia [YYYY]: ")
        pensja = input("pensja: ")
        pesel = input("PESEL")
        dataZatrudnienia = input("Data zatrudnnienia [YYYY-MM-DD]: ")

        self.c.execute("INSERT INTO pracownicy  (imie, nazwisko, rokUrodzenia, pensja, pesel, dataZatrudnienia) VALUES (%s,%s,%s,%s,%s,%s)", (imie, nazwisko, rokUrodzenia, pensja, pesel, dataZatrudnienia))
        czynapewno = input("na pewno dodać nowe dane [T]/[N]\n")
        if (czynapewno == "T" or czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie dodano")
        else:
            self.conn.rollback()
            print("Anlowano")

    def select(self):
        self.c.execute("SELECT * FROM pracownicy")
        Resoult = self.c.fetchall()

        print("%10s|%10s|%10s|%10s|%10s|%12s|%10s" % ("ID", "Imię", "Nazwisko", "RokUr.", "Pensja", "PESEL", "Data zatr."))
        for row in Resoult:
            print("%10s|%10s|%10s|%10s|%10s|%12s|%10s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def usun(self):
        self.select()
        pesel = input("Podaj PESEL osoby, którą chcesz usunąć: ")
        sql = ("DELETE FROM pracownicy WHERE pesel = %s" % (pesel))
        self.c.execute(sql)

        czynapewno = input("na pewno USUNĄC kmiota? [T]/[N]\n")
        if (czynapewno == "T" or czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie wywalono")
        else:
            self.conn.rollback()
            print("Anlowano")


    def aktualizuj(self):
        self.select()
        pesel = input("Podaj PESEL osoby, którą chcesz edytować: ")
        column = input("Którą kolumnę chcesz edytować?: ")
        value = input("Podaj nową wartość: ")
        sql = ("UPDATE pracownicy SET {}=%s WHERE pesel = %s").format(column)
        self.c.execute(sql, (value, pesel))

        czynapewno = input("na pewno edytować dane [T]/[N]\n")
        if (czynapewno == "T" or czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie zaktualizowano")
        else:
            self.conn.rollback()
            print("Anlowano")


    def menu(self):
        while(True):
            dec = input("<P> pokaż | <U> suń | <D> odaj | <A> ktualizuj | <W> yjdz\n")

            if (dec == "p" or dec == "P"):
                self.select()
            elif (dec == "d" or dec == "D"):
                self.insert()
            elif (dec == "u" or dec == "U"):
                self.usun()
            elif(dec == "a" or dec == "A"):
                self.aktualizuj()
            elif (dec == "w" or dec == "W"):
                print("wyszłem")
                break

ob = Pracownicy()
