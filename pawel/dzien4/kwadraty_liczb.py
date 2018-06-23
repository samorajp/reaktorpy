f = open("kwadraty.txt", "w")
suma=0
suma1=0
suma2=0
suma3=0
for i in range(-100,101):
    print(i, i**2)
    suma +=i**3
    suma1+=i
    suma2+=i**2
    suma3+=i**3
    napis = "%6s %6s %9s %9s %9s %9s %9s \n" % (i, i**2, i**3, suma, suma1, suma2, suma3)
    #napis2= " %s  %s  %s" %(suma1, suma2, suma3)
    f.write(napis)
saldo =str((suma1, suma2, suma3))
f.write(saldo)
f.close()