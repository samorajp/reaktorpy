import random

sekret = random.randint(1, 10)
#jeszcze_zgadujemy = True
proba = 1


while True and proba <=3:
    wpisana = int(input('Twój strzał: \n'))
    if wpisana == sekret:
        print('Wygrałeś w probie', proba)
        break
        #jeszcze_zgadujemy = False
    else:
        print('Nie trafiles')
        proba = proba +1

        if wpisana < sekret:
            print('Następnym razem podaj większą liczbę')
        else:
            print('Następnym razem podaj mniejszą liczbę')

        print('To twoja ', proba, 'proba')

# algorytm bisekcji