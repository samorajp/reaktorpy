def zarobek(kp, oprocentowanie, liczba_lat):
    print("Poczekaj, liczę. ")

    return round(kp*(1+(oprocentowanie/100))**liczba_lat,2)

kasa=int(input("Ile masz kasy? :"))
oprocentowanie = float(input("Jakie jest oprocentowanie?: "))
liczba_lat = int(input("Na ile lat?:"))

print(zarobek(kasa, oprocentowanie, liczba_lat))