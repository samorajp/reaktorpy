Liczby={1:'I', 2:'II',3:'III',4:'IV',5:'V',6:'IV',7:'VII',8:'VIII',9:'IX',10:'X'}

napis=input("Wpisz liczbę rzymską :")
cyfra_dziesiatek=int(napis[-2])
cyfra_jednosci=int(napis[-1])
jednosci_rzymskie= Liczby[cyfra_jednosci]
dziesiatki_rzymskie= 'X' * cyfra_dziesiatek



print(dziesiatki_rzymskie+jednosci_rzymskie)