# SPK = float(input("Podaj stan początkowy konta\n"))
# P = float(input("Jaka jest stopa procentowa (podaj w %): \n"))
# N = float(input("Ile lat chcesz oszczędzać: \n"))
#
# wynik = SPK*(1+P/100)**N
#
# print(wynik)
#


def zarobek(kp, oprocentowanie, liczba_lat):
    return round(kp*(1+oprocentowanie/100)**liczba_lat, 2)

kasa = float(input('Ile masz kasy?'))
oprocentowanie = float(input('Jakie jest oprocentowanie?'))
liczba_lat = int(input('Na ile lat?'))

wynik = zarobek(kasa, oprocentowanie, liczba_lat)


print(wynik)