# student (imie, nazwisko, nr_indeksu)

class Student:
   def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu

   def przedstaw_sie(self):
        print("Dzien dobry, Nazywam się %s %s a mój numer indeksu to %s" % (self.imie, self.nazwisko, self.nr_indeksu))


   def dane_do_raportu(self):
         print("%-10s %-10s %-8s"%(self.imie , self.nazwisko, self.nr_indeksu))

class Dziekanat:
    def __init__(self, imie_kierownika):
        self.imie_kierownika = imie_kierownika
        self.lista_studentow = []




    def dodaj_studenta(self, student):
        self.lista_studentow.append(student)

    def usun_studenta(self, nr_indeksu):
        do_usuniecia = None
        for student in self.lista_studentow:
            if student.nr_indeksu == nr_indeksu:
                do_usuniecia = student
                break

        print("Będę usuwał")
        print(do_usuniecia.dane_do_raportu())
        self.lista_studentow.remove(do_usuniecia)
    def pokaz_studenta(self):
        print("Wykaz studentów uczelni")
        #print(self.lista_studentow)


        for student in self.lista_studentow:
            student.dane_do_raportu()
        print("Sporządziła Pani %s" % self.imie_kierownika)


    def dodawanie_studenta_dla_pani_basi(self):
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        nr_indeksu = input(" Podaj numer indeksu: ")
        nowy_student = Student(imie, nazwisko, nr_indeksu)
        self.dodaj_studenta(nowy_student)

# student1 = Student("Adam", "Abacki", "123456")
# student1.przedstaw_sie()
# student2= Student("Balbuna", "Babacka","1213333")
dziekanat = Dziekanat("Basia")
# dziekanat.dodaj_studenta(student1)
# dziekanat.dodaj_studenta(student2)
# dziekanat.pokaz_studenta()
#
# dziekanat.usun_studenta(("1213333"))
while True:
    dziekanat.dodawanie_studenta_dla_pani_basi()
    dziekanat.pokaz_studenta()
