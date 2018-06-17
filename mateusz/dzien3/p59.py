import random

def losowe_zdanie(liczba_slow=5):
    wyrazy = ['Adam', 'Natalia', 'jabłko', 'je', 'żuk']
    wynik = ''
    for i in range(liczba_slow):
        wyraz = random.choice(wyrazy)
        wynik = wynik + wyraz + ' '
    wynik += '.'
    return wynik

#  po wykonaniu funkcji możemy odwołać się tylko do tego, co jest po def, tj. losowe_zdanie


print(losowe_zdanie(1))

