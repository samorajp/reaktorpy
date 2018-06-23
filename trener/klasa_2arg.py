class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dlugosc(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return "Wektor [%s, %s]" % (self.x, self.y)

    def __add__(self, other):
        nowy_x = self.x + other.x
        nowy_y = self.y + other.y
        return Wektor(nowy_x, nowy_y)

w1 = Wektor(1, 2)
w2 = Wektor(4, 8)


print(w1 + w2)