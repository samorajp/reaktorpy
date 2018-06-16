liczby =[]

liczby.append(1)
liczby.append(2)
liczby.append(3)
liczby.append(13)

imiona = []

imiona.append('Michał')
imiona.append('Monika')
imiona.append('Kuba')
imiona.append('Paweł')
imiona.append('Dawid')
imiona.append('Trener')

imiona.append('Ewa')
imiona.append('Adam')

imiona2 = []
imiona2 += ['Michał', 'Monika', 'Kuba', 'Paweł', 'Dawid', 'Trener', 'Ewa', 'Adam']

megalista = [liczby, imiona]

imiona3 = []
imiona3.extend(['Michał', 'Monika', 'Kuba', 'Paweł', 'Dawid', 'Trener', 'Ewa', 'Adam'])

print(liczby)
print(imiona)
print(megalista)
print("\n")
print(imiona2)
print(imiona3)
print(liczby, imiona, megalista)
print("\n", "usuwanie", "\n")
imiona.pop()
print(imiona)
imiona.pop(2)
print(imiona)