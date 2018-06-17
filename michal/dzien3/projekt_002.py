# lista = [1, 2, 3, 'rabarbar', 5, 6, 7, 8, 9,]
#
# for liczba in lista:
#     print(liczba, liczba*2)

# for i in range(3, 10):
#     print(i, i ** 2)

# krotka = ('chlep', 'maslo', 'japko')
# for jedzenie in krotka:
#     print(jedzenie)

# slownik = {'Adam': 7, 'Ewa': 15, 'Belzebub': 5}
# for x in slownik:
#     print(x)
#     print(x, slownik[x])

for x in range(1, 11):
    for alfa in range(1, 11):
        print('mnożenie ' + str(x) + ' * ' + str(alfa) + "= " + str(alfa*x))
    print("\n")