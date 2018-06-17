import datetime

def zegar(godzina='brak', minuta='brak'):
    if godzina == 'brak' and minuta == 'brak':
        aktualny_czas = datetime.datetime.now()
        # mamy pewność, że nie podał nic
        godzina = aktualny_czas.hour
        minuta = aktualny_czas.minute


    uplynelo_godzin = godzina - 9
    uplynelo_minut = minuta - 0
    krotka_od_poczatku = uplynelo_godzin, uplynelo_minut

    pozostalo_godzin = 7 - uplynelo_godzin
    pozostalo_minut = 60 - uplynelo_minut

    if pozostalo_minut == 60:
        pozostalo_minut = 0
        pozostalo_godzin += 1

    krotka_do_konca = pozostalo_godzin, pozostalo_minut
    return krotka_do_konca, krotka_od_poczatku

print(zegar())
# print(zegar(16, 46) == ((0 , 14), (7, 46)))

while True
