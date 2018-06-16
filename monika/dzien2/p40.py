slownik = {'1' : 'I',
           '2' : 'II',
           '3' : 'III',
           '4' : 'IV',
           '5': 'V',
           '6': 'VI',
           '7': 'VII',
           '8': 'VIII',
            '9': 'IX',
           '10': 'X',

           }



cyfry = input("Wpisz liczbe dziesietna: ")



cyfra_dziesiatek = cyfry [-2]
cyfra_jednosci = cyfry [-1]

jednosci_rzymskie = slownik[cyfra_jednosci]
dziesiatki_rzymskie = "X" * int(cyfra_dziesiatek)

print(dziesiatki_rzymskie + jednosci_rzymskie)
