kwota = 999
vat3 = 0.03
vat7 = 0.07
vat23 = 0.23

print("kwota brutto", kwota)
print("netto przy vat 3%", round(kwota - kwota * vat3, 2))
print("netto przy vat 7%", round(kwota - kwota * vat7, 2))
print("netto przy vat 23%", round(kwota - kwota * vat23, 2))