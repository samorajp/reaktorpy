import random
sekret = random.randint(1,1000)
#
# wpisana = int(input("Twój strzał: "))
# if wpisana == sekret:
#     print("WYGRAŁEŚ !")
# else:
#     print("NIE TRAFIŁEŚ. CHODZIŁO O ",sekret)

jeszcze_zgadujemy = True
proba = 1
while jeszcze_zgadujemy and proba <=10:
    wpisana = int(input("Twój strzał: "))
    if wpisana == sekret:
        print ("WYGRAŁEŚ W PRÓBIE", proba)
        jeszcze_zgadujemy = False
    else:
        print("NIE TRAFIŁEŚ")
        proba +=1

        if wpisana < sekret:
            print("Za mała!")
        else:
            print("Za duża")
print(sekret)

