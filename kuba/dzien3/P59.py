import random

def losowe_zdanie(liczba_słów=5): # =5 jest domyślną ilością słów lae możemy zmienić ją na dole 11 linijka
    wyrazy = ['Adam', 'Natalia', 'jabłko', 'je', 'żuk']
    wynik =""
    for i in range(liczba_słów):
        wyraz = random.choice(wyrazy)
        wynik +=wyraz + " "
    wynik += "."
    return wynik
print(losowe_zdanie(3))