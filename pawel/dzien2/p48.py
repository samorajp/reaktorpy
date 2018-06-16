# wartość=int(input("Wprowadź liczbę:  "))
# if wartość%2 ==0 and wartość%3==0:
#     print("Parzysta, podzielna przez 3")
#     if wartość%2 == 0 and wartość%3 !=0:
#         print( "PARZYSTA i nic więcej")
#         if wartość%2 != 0 and wartość%3 ==0:
#             print( "Podzielna przez 3 i nic więcej")
#
# else:
#     print('NIEPARZYSTA')

wartość = int(input("Wprowadź liczbę:  "))
if wartość % 2 == 0 and wartość % 3 == 0:
    print("Parzysta i podzielna przez 3")
elif wartość % 2 == 0 and wartość % 3 != 0:
    print("PARZYSTA i nic więcej")
elif wartość % 2 != 0 and wartość % 3 == 0:
    print("Podzielna przez 3 i nieparzysta")
else:
 print('NIEPARZYSTA i nic więcej')
