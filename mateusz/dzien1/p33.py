SPK = float(input("Podaj stan początkowy konta\n"))
P = float(input("Jaka jest stopa procentowa (podaj w %): \n"))
N = float(input("Ile lat chcesz oszczędzać: \n"))

wynik = SPK*(1+P/100)**N

print(wynik)



