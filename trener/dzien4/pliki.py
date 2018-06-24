nowy_plik = open("niemiecki.txt", "w")
nowy_plik.write("TU BĘDZIE MOJE ROMEO I JULIA\n")

f = open("romeo.txt")
lista_linii = f.readlines()
f.close()


lista_linii = lista_linii[:20]


for linia in lista_linii:
    nowy_plik.write(linia.upper())
nowy_plik.close()

