import random

def losowe_zdanie(liczba_slow=5):
    wyrazy = ['Adam', 'Natalia', 'jabłko', 'je', 'żuk']
    wynik = ""
    for i in range(liczba_slow):
        wyraz = random.choice(wyrazy)
        wynik += wyraz + " "
    wynik += "."
    return wynik


po_wykonaniu_funkcji = losowe_zdanie(7)
print(po_wykonaniu_funkcji)