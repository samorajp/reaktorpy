import random
sekret = random.randint(1, 2)

wpisana = int(input('Twój szczał: \n'))

if wpisana == sekret:
    print('wgrałeś')
else:
    print("Źle!! poprawna liczba to", sekret)