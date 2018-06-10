kwota = 999
vat3 = 0.03
vat7 = 0.07
vat23 = 0.23

print("kwota brutto", kwota)
print("netto przy vat 3%", round(kwota / (1 + vat3), 2))
print("netto przy vat 7%", round(kwota / (1 + vat7), 2))
print("netto przy vat 23%", round(kwota / (1 + vat23), 2))

print("\n")
brutto = 999
stawka = 0.03
netto = brutto * stawka
zaokraglone = round(netto, 2)

print(zaokraglone)