wiek = int(input('Ile masz lat? '))


if wiek < 18:
    print('Idź spać!')
elif wiek<50:
    print('Jesteś młody')
elif wiek<70:
    print('Jesteś już dość stary')
elif wiek<90:
    print('Jesteś najstarszy')
else:
    print('Idź spać')
    