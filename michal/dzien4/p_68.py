from random import randint

print(randint(0, 49))

class Lotek:
    def __init__(self):
        self.liczby = set()

    def losuj(self):
        while len(self.liczby) <= 6:
            self.liczby.add(randint(0, 49))
            print(self.liczby)
        print(self.liczby)


obj = Lotek()

obj.losuj()
