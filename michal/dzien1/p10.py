Chleb = 1.99
Mleko = 2.50
Cukierki = 12.99

zam_ch = 2
zam_ml = 0.5
zam_cu = 0.3
tekst = "Wartość zamówienia to: "

zamowienie = round(zam_ch * Chleb + zam_ml * Mleko + zam_cu * Cukierki, 2)

print(tekst, zamowienie)