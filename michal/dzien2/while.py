import random
sekret = random.randint(1, 10)
strzal = 3

# if wpisana == sekret:
#     print('wgrałeś')
# else:
#     print("Źle!! poprawna liczba to", sekret)

jeszcze_zgadujemy = True
proba = 1

while jeszcze_zgadujemy and  proba <= 3:
    wpisana = int(input('Twój szczał: \n'))
    if wpisana == sekret:
        print('wygrałeś')
        jeszcze_zgadujemy = False
    else:
        print('przegrałeś\nzostało ci ' + str(3 - proba) + " szans" )
        proba += 1 # proba = proba + 1