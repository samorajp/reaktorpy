liczby = []
liczby.append(1)
liczby.append(2)
liczby.append(3)


imiona = ["zerowy element listy"]

# imiona.append("Adam")
# imiona.append("Ewa")

imiona += ["Adam", "Ewa"] # zamiast dwa razy append do pustej list
imiona *= 2
# imiona.extend(["Adam", "Ewa"])  # to samo co wyżej, zamiast dwa razy append trener/dzien2

print(liczby)
print(imiona)

# nowalista = []
# nowalista.append(liczby)
# nowalista.append(imiona)
nowalista = [liczby, imiona]  # to samo co wyżej, zamiat dwa razy append do pustej listy
print(nowalista)