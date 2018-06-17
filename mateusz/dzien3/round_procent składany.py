def zarobek(kp, oprocentowanie, liczba_lat):
    print('Poczekaj liczę')
    return round(kp*(1+oprocentowanie/100)**liczba_lat, 2)

kasa = float(input('Ile masz kasy?'))
oprocentowanie = float(input('Jakie jest oprocentowanie?'))
liczba_lat = int(input('Na ile lat?'))

wynik = zarobek(kasa, oprocentowanie, liczba_lat)


print(wynik)