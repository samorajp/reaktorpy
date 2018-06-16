imie = 'Jan'
nazwisko = 'Kowalski'
wiek = 100
pensja = 1234
stanowisko = 'stażysta'

pensjanapis = str(pensja)
wieknapis = str(wiek)

# - tak nie, bo nie da się pomnożyć tego
# print ('Pan ', imie, ' ', nazwisko, '(', 'wiek: ', wiek, ' lat ) pracuje na stanowisku ',stanowisko, ' (pensja: ', pensja, ' brutto)')


dane_os = 'Pan ' + imie + ' ' + nazwisko + '(' + 'wiek: ' + wieknapis + ' lat ) pracuje na stanowisku ' + stanowisko + ' (pensja: ' + pensjanapis + ' brutto)' + '\n'

print(dane_os*10)