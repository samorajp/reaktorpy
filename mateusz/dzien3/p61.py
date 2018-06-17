

def suma_i_wyraz(n, a1=1, q=2):
    suma=0
    # a1, q, n -> będzie wpisane przez kogoś, kto użyje funkcji
    aktualny_wyraz = a1

    for i in range(n):
        suma = suma + aktualny_wyraz
        aktualny_wyraz = aktualny_wyraz * q

    return suma, aktualny_wyraz /q

print(suma_i_wyraz(4,3,2))
