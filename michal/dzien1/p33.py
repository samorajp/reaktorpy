print("oblicze twój stan konta po 'N' latach z roczną kapitalizacja odsetek")

kap_pocz = int(input("Podaj poczatkowy stan konta: \n"))
R = float(input("Podaj roczną stopę procentową jako ułamek dziesiętny oddzielony kropką:\n"))
lata = int(input("Podaj liczbę lat\n"))

kap_kon = kap_pocz * (1 + R)**lata

print("kapitał końcowy to:", kap_kon)