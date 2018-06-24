F = open('nazwa.txt', 'w')
L = ['Ala\n', 'ma\n', 'kota\n']
F.writelines(L)
F.close()

F = open('nazwa.txt', 'r')
for linia in F:
    print(linia, end='')
F.close()