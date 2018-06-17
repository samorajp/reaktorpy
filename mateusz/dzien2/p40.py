rzymskie={  0:'',
            1:'I',
            2:'II',
            3:'III',
            4:'IV',
              5:'V',
               6:'VI',
               7:'VII',
               8:'VIII',
               9:'IX',
        10: 'X'}

cyfry = input('Podaj liczbe: ')

cyfra_jednosci=int(cyfry[-1])
cyfra_dziesiatek=int(cyfry[-2])


jednosci_rzymskie=rzymskie[cyfra_jednosci]
dziesiatki_rzymskie='X'*cyfra_dziesiatek


print(dziesiatki_rzymskie + jednosci_rzymskie)




# print(rzymskie[int(cyfry)])