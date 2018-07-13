class Pracownicy:
    def __init__(self):
        self.listaPracownik = [("adam", "śmiały", "K", 1500),
                               ("józef", "blady", "K", 2500),
                               ("denis", "dżonson", "K", 1500)]

    def pokazPracownika(self):
        for i in self.listaPracownik:
            print(i)

    def usunPracownika(self, id_del):

        for index, wartosc in enumerate(self.listaPracownik):
            if wartosc[0] == id_del:
                self.listaPracownik.pop()

    def zmienPracownika(self, id_zm):

        print(self.id_zm)

class Firma(Pracownicy):
    def __init__(self, firma):
        super().__init__()
        self.nazwaFirmy = firma

    def Menu(self):
        while(True):
            dec = input("| <D>  | <P> okaż | <U> suń | <Z> mień | <W> yjdż |\n")

            if (dec == "P" or dec == "p"):
                self.pokazPracownika()

            elif (dec == "U" or dec == "u"):
                id_del = input("Podaj ID pracownika: ")
                self.usunPracownika(id_del)
                self.pokazPracownika()


            elif (dec == "W" or dec == "w"):
                print("Dzięki za wspaiałą współpracę! Do jutra!")
                break

ob = Firma("ZPR")

ob.Menu()