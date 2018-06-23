def odleglosc(a, b, c, d):
    pierwszy = ((a-c)**2)
    drugi = ((b-d)**2)
    x = (pierwszy + drugi)**0.5
    return x


print("Liczenie odległości między punktami na płaszczyźnie")
while True:

    a = int(input("Wpisz pierwszą daną pierwszego punktu: "))
    b = int(input("Wpisz drugą daną pierwszego punktu: "))
    c = int(input("Wpisz pierwszą daną drugiego punktu: "))
    d = int(input("Wpisz drugą daną drugiego punktu: "))

    x = odleglosc(a, b, c, d)

    #print("Odległość między punktami to: ", x)
    print("Odległość między punktami to: ", "%.2f" % (x))
    print("Czy chcesz sprawdzać dalej odległości między punktami ? ")
    odpowiedź = input("tak/nie")
    if odpowiedź == "tak":
     print("No to dawaj ! ;) ")
    else:
     print("TO NIE ! :( ")
     break

# Niestety ładny zaokrąglony wynik nie chce zadziałać :/

