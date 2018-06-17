slownik = {1: 'I',
           2: 'II',
           3: 'III',
           4: 'IV',
           5: 'V',
           6: 'VI',
           7: 'VII',
           8: 'VIII',
           9: 'IX',
           10: 'X',
}

cyfry = input("Wpisz liczbe dziesietna: ")  # = "67"

cyfra_dziesiatek = cyfry[-2] # "6"
cyfra_jednosci = cyfry[-1] # "7"
do_szukania_jednosci = int(cyfra_jednosci) # 7
do_mnozenia_X = int(cyfra_dziesiatek) # 6

jednosci_rzymskie = slownik[do_szukania_jednosci]     # 'VII'
dziesiatki_rzymskie = "X" * do_mnozenia_X

print(dziesiatki_rzymskie + jednosci_rzymskie)
#####  "XXXXXX" + "VIII" =  "XXXXXXVIII"
