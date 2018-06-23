class Dziekanat:
    def __init__(self,imie_kierownika):
        self.imie_kierownika = imie_kierownika
        self.lista_studentow = []

    def dodaj_studenta(self,student):
        self.lista_studentow.append(student)
        pass
    def usuń_studenta(self, nr_indeksu):
        do_usuniecia = None
        for student in self.lista_studentow:
            if student.nr_indeksu == nr_indeksu:
                do_usuniecia = student
                break
        print("Będę usuwał")
        do_usuniecia.dane_do_raportu()
        self.lista_studentow.remove(do_usuniecia)

    def pokaż_studentów(self):
        print("WYKAZ STUDENTÓW UCZELNI")
        #print(self.lista_studentow)
        for student in self.lista_studentow:
            student.dane_do_raportu()
        print("Sporządziła Pani %s" % self.imie_kierownika)

    def dodawanie_studenta_dla_pani_basi(self):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        nr_indeksu = input("Podaj numer indeksu: ")
        nowy_student = Student(imie, nazwisko, nr_indeksu)
        self.dodaj_studenta(nowy_student)


class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie=imie
        self.nazwisko=nazwisko
        self.nr_indeksu=nr_indeksu

    def przedstaw_sie(self):
        print("Dzień dobry. Nazywam się %s %s, mój numer indeksu to %s." %
              (self.imie, self.nazwisko, self.nr_indeksu))
    def dane_do_raportu(self):
        print("%-10s %-10s %-8s" % (self.imie, self.nazwisko, self.nazwisko))

# student1 = Student("Adam", "Abacki", "123456")
# student2 = Student("Balbuna", "Babacka", "234567")
# student1.przedstaw_sie()
#
# dziekanat = Dziekanat("Basia")
#
# dziekanat.dodaj_studenta(student1)
# dziekanat.dodaj_studenta(student2)
# dziekanat.pokaż_studentów()
#
# dziekanat.usuń_studenta("234567")

dziekanat = Dziekanat("Basia")
while True:
    dziekanat.dodawanie_studenta_dla_pani_basi()
    dziekanat.pokaż_studentów()