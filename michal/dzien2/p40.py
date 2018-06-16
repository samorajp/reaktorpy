slownik = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
}

napis = input('wpisz liczbe w systemie dziesietnym\n')
#napis = "22"

c_j = int(napis[-1])
c_d = int(napis[-2])
l_rz = str(slownik[10] * c_d) + str(slownik[c_j])

print(l_rz)
