def procent_skladany (kapital_pocz, oprocentowanie, liczba_lat):
    return round(kapital_pocz * (1 + oprocentowanie) ** liczba_lat, 2)


print("oblicze twój stan konta po 'N' latach z roczną kapitalizacja odsetek")

kp = int(input("Podaj poczatkowy stan konta: \n"))
op = float(input("Podaj roczną stopę procentową jako ułamek dziesiętny oddzielony kropką:\n"))
ll = int(input("Podaj liczbę lat\n"))



print("kapitał końcowy to:", procent_skladany (kp, op, ll))