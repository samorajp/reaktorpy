class Kursant:
    ile_nas_jest =0
    def __init__(self,imie_podane, nazwisko_podane):
        self.imie= imie_podane
        self.nazwisko = nazwisko_podane
        self.energia = 100
        Kursant.ile_nas_jest +=1
        print("Tworzony jest nowy kursant.")

    def __str__(self):
        napis = """Kursant: %s %s 
        Energia: %s
        """ % (self.imie, self.nazwisko, self.energia)
        return napis

    def pokaz_ladnie_imie_kursanta_(self):
        if self.energia>=10:
            print("Jestem: %s" % (self.imie))
            self.energia = self.energia -10
        else:
            print("Jestem zmęczony(a).")

    def zjedz_jablko(self):
        print("Zjadłem jabłuszko.")
        self.energia = 100

class KursantWytrwaly(Kursant):
    def __init__(self, imie, nazwisko):
        super(). __init__(imie, nazwisko)
        self.energia = 200

kursant1 = KursantWytrwaly("Jan", "Kowalski")
kursant2 = Kursant("Aldona", "Marcinkiewicz")

for i in range(21):
    kursant1.pokaz_ladnie_imie_kursanta_()
    print(kursant1)

kursant1.zjedz_jablko()
kursant1.pokaz_ladnie_imie_kursanta_()