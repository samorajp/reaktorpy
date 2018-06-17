# import random
#
# n = 3
#
# wyrazy = ['Adams', 'Natalia', 'japko', 'je', 'żuku']
# wynik = ''
# for i in range(3):
#     wyraz = random.choice(wyrazy)
#     wynik += ' ' + wyraz + '.'
#     print(wynik)
# print(wynik)

import random
def losowe_zdanie(liczba_slow):
    wyrazy = ['Adams', 'Natalia', 'japko', 'je', 'żuku']
    wynik = ''
    for i in range(liczba_slow):
        wyraz = random.choice(wyrazy)
        wynik += ' ' + wyraz
    wynik += '.'
    return(wynik)

print(losowe_zdanie(3))