suma=0
wartość =0
j = 0
while True:
    print("Podaj liczbę: ")
    minsup = int(input())




    if minsup in range(-1000,1000):
        print("Ile wartości zliczyć ?")
        j =int(input())
        if j >=1000:
            print("Za duża wartość")
    suma += minsup
    minsup += 1
    if wartość >=j:
        continue
    else:
        print("Podałeś wartość poza skalą. Czy chcesz podać inną wartość ? ")
        zapytanie =(input())
        if zapytanie == "tak":
         print("No to zapraszam :)")
        else:
         print("TO NIE !")

print(suma)
