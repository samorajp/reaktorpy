# liczba1 = None
#
# napis = input("Podaj liczbę:")
# if napis.isdigit():
#     liczba1 = int(napis)
#
# liczba2 = None
# napis = input("Podaj liczbę:")
# if napis.isdigit():
#     liczba2 = int(napis)
#
# print(liczba1 + liczba2)
#
# x = wez_liczbe()
# y = wez_liczbe()



def wykonaj_dzialania(x, y):
    return [x+y, x-y, x*y, x/y]

lista = wykonaj_dzialania(6, 2)
print(lista[3])
