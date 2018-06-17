rzymskie ={ 1:'I', 2:'II', 3:'III', 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:'IX', 10:"X"}
cyfra = input("podaj liczbę: ")
#po_rzymsku = rzymskie[liczba]
#print(po_rzymsku)

#cyfra 28

cyfra_dziesiatek = int(cyfra[-2])# przedostatnia cyfra, przdostatni znak zamieniona na cyfrę
cyfra_jedności= int(cyfra[-1])
jednosci_rzymskie=rzymskie[cyfra_jedności]
dziesiatki_rzymskie='X'*cyfra_dziesiatek

print(dziesiatki_rzymskie+jednosci_rzymskie)