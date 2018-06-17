a1=1
q=2

def suma_i_wyraz(n,a1=1,q=2):
    suma=0
    aktualny_wyraz =a1
    for i in range(n):
        suma+= aktualny_wyraz
        aktualny_wyraz*=q
    return suma, aktualny_wyraz /q
print(suma_i_wyraz(4,3,2))

def suma_i_wyraz2 (n, a1=1, q=2):
    licznik= 1- q ** n
    mianownik = 1-q
    wynik = a1 * licznik/mianownik
    return wynik, a1* q **(n-1)

print(suma_i_wyraz(2,3,5) == suma_i_wyraz2(2,3,5))
print(suma_i_wyraz(2,3,5))
print(suma_i_wyraz2(2,3,5))

