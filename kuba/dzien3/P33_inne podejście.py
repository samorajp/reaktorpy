def zarobek(kp, oprocentowanie, liczba_lat):
    print("Poniżej wynik")
    return kp*(1+oprocentowanie/100)**liczba_lat

kasa = int(input("Ile masz kasy ? "))
oprocentowanie= float(input("Jakie jest oprocentowanie ? "))
liczba_lat = int(input("Na ile lat ? "))

print(round(zarobek(kasa, oprocentowanie, liczba_lat),2))