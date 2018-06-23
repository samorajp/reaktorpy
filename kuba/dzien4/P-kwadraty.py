f = open("kwadraty.txt","w")
suma = 0
suma2 = 0
suma3 = 0
for i in range(1,101):
    suma += i
    suma2 += i**2
    suma3 += i**3
    napis = ("%5s,%6s,%7s,%8s,%9s,%10s\n" % (i,i**2,i**3, suma, suma2, suma3))
    f.write(napis)
f.close()