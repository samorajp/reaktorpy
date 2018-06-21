a1 = 1
q = 2

def suma_i_wyraz(n, a1=1, q=2):
    suma = 0
    aktualny_wyraz = a1
    for i in range(n):
        suma += aktualny_wyraz
        aktualny_wyraz *= q
    return suma, aktualny_wyraz / q

def suma_i_wyraz2(n, a1=1, q=2):
    licznik = 1 - q ** n
    mianownik = 1 - q
    wynik = a1 * licznik / mianownik
    return wynik, a1 * q ** (n-1)

krotka = suma_i_wyraz(4,3,2)
print(krotka)
print(krotka[0] + krotka[1])

print(suma_i_wyraz(100, 6, 3) == suma_i_wyraz2(100, 6, 3))
print(suma_i_wyraz(11, 6, 3))
print(suma_i_wyraz2(11, 6, 3))