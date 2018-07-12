class Zawodnik:

    def  __init__(self, imie, wzrost, waga):
        self.name = imie
        self.h = wzrost
        self.masa = waga

    def obliczBMI(self):
        bmi = round((self.masa / (self.h * self.h) * 10000), 0)
        return bmi
    def wyswietlBMI(self):
        bmi2 = round((self.masa / (self.h * self.h) * 10000), 0)
        poka = self.name + bmi2
        return poka


Obj1 = Zawodnik("Jan", 175, 95)
print(Obj1.obliczBMI())
print(Obj1.wyswietlBMI())