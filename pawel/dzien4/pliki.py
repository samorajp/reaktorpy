f = open("romeo.txt")

linia = f.readline()
print(linia)

nowy_plik = open("niemiecki.txt", "w")
lista_linii = f.readlines()
lista_linii = lista_linii[:20]
for linia in lista_linii:
    print(linia)


    nowy_plik.write(linia.upper())
nowy_plik.close()