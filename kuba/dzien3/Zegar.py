import datetime

def zegar (godzina="Brak",minuta="Brak"):

    if godzina=="Brak" and minuta == "Brak":
        godzina = datetime.datetime.now().hour
        minuta = datetime.datetime.now().minute

    upłynelo_godzin=godzina-9
    uplynelo_minut=minuta -0
    krotka_od_poczatku = upłynelo_godzin, uplynelo_minut

    pozostało_godzin=7-upłynelo_godzin
    pozostało_minut=60-uplynelo_minut

    if pozostało_minut ==60:
        pozostało_minut =0
        pozostało_godzin +=1
    krotka_do_konca=pozostało_godzin,pozostało_minut
    return krotka_do_konca, krotka_od_poczatku

print(zegar())
print(zegar(16,46) == ((0,14),(7,46)))


