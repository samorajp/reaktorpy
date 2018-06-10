brutto=3000
vat1=0.03
vat2=0.08
vat3=0.23

netto = brutto/(1+vat3)
zaokr = round(netto)
print(zaokr)


brutto=zaokr*(1+vat3)
print(round(brutto))