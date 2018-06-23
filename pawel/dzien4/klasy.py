class Kursant:
    ile_nas_jest = 0

    def __init__(self, imie_podane, nazwisko_podane):
        self.imie = imie_podane
        self.nazwisko = nazwisko_podane
        self.energia = 100
        print("Tworzony jest nowy kursant.")
        Kursant.ile_nas_jest += 1

    def pokaz_ladnie_imie_kursanta(self):
        if self.energia >= 10:
            print("Jestem %s" % self.imie)
            self.energia = self.energia - 10
        else:
            print("Jestem zmęczony(a).")

    def zjedz_jablko(self):
        print("Zjadłem jabłuszko.")
        self.energia = 100

    def __str__(self):
        napis = """Kursant: %s %s
        Energia: %s
        """ % (self.imie, self.nazwisko, self.energia)
        return napis

class KursantWytrwaly(Kursant):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)
        self.energia = 200

kursant1 = KursantWytrwaly("Jan", "Kowalski")
kursant2 = Kursant("Alina", "Kowalska")

for i in range(11):
    kursant1.pokaz_ladnie_imie_kursanta()
    print(kursant1)

kursant1.zjedz_jablko()
kursant1.pokaz_ladnie_imie_kursanta()



class Lista:
    def append(self, x):
        pass
