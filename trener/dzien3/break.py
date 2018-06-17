import random
sekret = random.randint(1, 6)
proba = 1

while True:
    wpisana = int(input("Twój strzał: "))
    if wpisana == sekret:
        print("WYGRAŁEŚ W PRÓBIE", proba)
        break
    else:
        print("NIE TRAFIŁEŚ")
        if wpisana < sekret:
            print("Za mała!")
        else:
            print("Za duża")
        proba += 1
        if proba > 3:
            break


print(sekret)