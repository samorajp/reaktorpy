class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Soft(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__( nazwa, cena)
        self.jezyk = jezyk
        self.system = system

class Szkolenia(Soft):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def wyprintuj(self):
        print(self.nazwa, self.cena, self.jezyk, self.system, self.termin)


ob = Szkolenia("PHP 3 w dni", 150, "PHP", "WINDOWS", "dziś")

ob.wyprintuj()

