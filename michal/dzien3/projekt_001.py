# liczba_0 = 0
# suma = 0
#
# while liczba_0 < 1000:
#     if liczba_0 %3  == 0 or liczba_0 % 5 == 0:
#         suma += liczba_0
#     liczba_0 += 1
# print('suma wszystkich liczb podzielnych przez 3 i 5 to: ' + str(suma))
a = sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0)
print(a)

