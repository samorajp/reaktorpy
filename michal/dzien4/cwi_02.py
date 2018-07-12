class Dziekanat:

    def  __init__(self):
        self.studenci = []

    def dodajStudenta(self, nr_indeksu, imie, nazwisko):
        self.studenci.append([nr_indeksu, imie, nazwisko])

    def listaStudentow(self):
        for i in self.studenci:
            print (i)

    def usunStudenta(self, nr_indeksu):
        for index, wartosc in enumerate(self.studenci):
            if wartosc[0] == nr_indeksu:
                self.studenci.pop()



ob = Dziekanat()

ob.dodajStudenta(12, "Marian", "Kowalski")
ob.dodajStudenta(35, "Olaf", "Ryś")
ob.dodajStudenta(77, "Jola", "Orlowsky")
ob.dodajStudenta(774, "Jola", "Orlowsky")

ob.listaStudentow()
print("\n")
ob.usunStudenta(774)
print("\n")
ob.listaStudentow()