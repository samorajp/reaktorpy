import random
sekret = random.randint(1, 1000)
jeszcze_zgadujemy = True
proba = 1

while jeszcze_zgadujemy and proba <= 10:
    wpisana = int(input("Twój strzał: "))
    if wpisana == sekret:
        print("WYGRAŁEŚ W PRÓBIE", proba)
        jeszcze_zgadujemy = False
    else:
        print("NIE TRAFIŁEŚ")
        if wpisana < sekret:
            print("Za mała!")
        else:
            print("Za duża")
        proba += 1
print(sekret)