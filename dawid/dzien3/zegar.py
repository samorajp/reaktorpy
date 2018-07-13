# zegar cwiczenie

import datetime
def zegar(godzina="brak", minuta="brak"):
    if godzina == "brak" and minuta == "brak":
        aktualny_czas=datetime.datetime.now()

    # uzytkownik jeszcze nie podał parametry
        godzina = aktualny_czas.hour
        minuta = aktualny_czas.minute

    upłynęło_godzin = godzina-9
    upłynęło_minut = minuta - 0
    krotka_od_początku = upłynęło_godzin, upłynęło_minut

    pozostało_godzin=7-upłynęło_godzin
    pozostało_minut=60 - upłynęło_minut
    if pozostało_minut ==60:
        pozostało_minut =0
        pozostało_godzin+=1

    krotka_do_końca= pozostało_godzin, pozostało_minut

    return krotka_do_końca, krotka_od_początku

#print(zegar(16,33))

print(zegar())
czas=datetime.datetime.now()