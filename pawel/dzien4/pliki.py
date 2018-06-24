f = open("dane.txt")

linia = f.readline()
print(linia)


lista_linii = f.readlines()
for linia in lista_linii:
    print(linia)