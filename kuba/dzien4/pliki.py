f=open("romeo.txt")

lista_linii = f.readlines()
lista_linii = lista_linii[:20]

nowy_plik = open("niemiecki.txt","w")

for linia in lista_linii:
    nowy_plik.write(linia.upper())
    print(linia)