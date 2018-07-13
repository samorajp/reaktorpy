class Pracownicy:
    def __init__(self):
        self.listaPracownik = []

    def dodajPracownika(self, imie, nazwisko, kontrakt, pensja):

        self.listaPracownik.append([imie, nazwisko, kontrakt, pensja])

    def pokazPracownika(self):
        for i, v in enumerate(self.listaPracownik):
            print(i, v[0], v[1], v[2], v[3])

    def usunPracownika(self, id_del):
        self.listaPracownik.pop(int(id_del))

    def zmienPracownika(self, id_zm):

        print(self.id_zm)

class Firma(Pracownicy):
    def __init__(self, firma):
        super().__init__()
        self.nazwaFirmy = firma

    def Menu(self):
        while(True):
            dec = input("| <D> odaj | <P> okaż | <U> suń | <Z> mień | <W> yjdż |\n")

            if (dec == "D" or dec == "d"):
                imie = input("Podaj imie nowego: ")
                nazwisko = input("Podaj nazwisko nowego: ")
                kontrakt = input("Podaj forme zatrudnienia nowego - [K] ontrakt - [S] tażysta: ")
                pensja = int(input("Podaj pensje nowego: "))
                self.dodajPracownika(imie, nazwisko, kontrakt, pensja)

            elif (dec == "P" or dec == "p"):
                self.pokazPracownika()

            elif (dec == "U" or dec == "u"):
                id_del = input("Podaj ID pracownika: ")
                self.usunPracownika(id_del)
                self.pokazPracownika()

            elif (dec == "Z" or dec == "z"):
                id_zm = input("Podaj ID pracownika do zmiany etatu: ")
                self.zmienPracownika(id_zm)

            elif (dec == "W" or dec == "w"):
                print("Dzięki za wspaiałą współpracę! Do jutra!")
                break

ob = Firma("ZPR")

ob.Menu()