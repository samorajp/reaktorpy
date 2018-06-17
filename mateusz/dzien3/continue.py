licznik = 1

while True:
    print(licznik)
    licznik += 1

    if licznik % 2 ==0:
        continue

    print('nie było continue')
    if licznik ==5:
        break



# continue -> powrót do pierwszej instruckji w pentli,  niezależnie od dalszych instrukcji