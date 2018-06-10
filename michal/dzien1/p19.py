imie = "Michał"
nazwisko = "Adamski"
data_ur = "31.01.1986"
stanowsiko = "bezrobotny"
placa = 0

wyswietl = imie + " " + nazwisko + " " + data_ur + " " + stanowsiko + " " + str(placa) + "\n"

print("1" + imie + " " + nazwisko + " " + data_ur + " " + stanowsiko + " " + str(placa)*10)
print("2" + (imie + " " + nazwisko + " " + data_ur + " " + stanowsiko + " " + str(placa))*10)
print("3" + imie, nazwisko, data_ur, stanowsiko, str(placa), sep=" - " )
print(("4" + imie, nazwisko, data_ur, stanowsiko, str(placa))*10, sep=" - " )

a = '999'
print('a')
print(print(wyswietl*10), sep="\n")

print(print(wyswietl, sep="\n")*10)