import random
sekret= random.randint(1,10)
jeszcze_zgadujemy=True
proba =1





while jeszcze_zgadujemy and proba<=3:

    wpisana= input("Twój strzał: ")
    if int(wpisana)==sekret:

        print("WYGRALES")
        jeszcze_zgadujemy= False
    else:
        print("NIE TRAFIŁEŚ.")
        if int(wpisana) > sekret:
                print("Podaj niższą wartość")
        else:
                print ("Podaj wyższą wartość")#PRACA DOMOWA TU W
        proba = proba+1


        #praca dommowa - dopisać w elsie ifa, który będzie nam mówił, czy liczba wprowadzona jest za mała czy za duża