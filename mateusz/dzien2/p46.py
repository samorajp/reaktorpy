def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def przywitanie(imie):
    print("\nWitaj")
    print(imie)

x = input('Podaj liczbę!\n')

#dlaczego float nie rozpoznaje kropki??

if is_number(x):
    if float(x) >=0 and float(x) <=9:
            print('Zgadza się!')
    else:
            print('Liczba spoza przedziału')
else:
        print('To nie jest liczba!')


przywitanie("Mateusz")