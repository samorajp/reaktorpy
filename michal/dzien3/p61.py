def ciag(n, a1 = 1, q = 2):
    suma = 0
    aktualny_wyraz = a1
    for i in range(n):
        suma += aktualny_wyraz
        aktualny_wyraz *= q
    return (suma, int(aktualny_wyraz/q))

print(ciag(4, 3, 2))

def ciag2 (n, a1 = 1, q = 2):
    licznik = 1 - q ** n
    mianownik = 1 - q
    wynik = a1 * licznik / mianownik
    return wynik, a1 * q ** (n-1)