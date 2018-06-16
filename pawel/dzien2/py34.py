liczby =[]
liczby.append(1)
liczby.append(2)
liczby.append(3)
imiona=[]
imiona.append("Adam")
imiona.append("Ewa")
print(liczby)
print(imiona)

#drugie rozwiązanie to  imiona.extend("Adam", "Ewa")  zamiast append do pustej listy razy dwa
#trzecie rozwiązanie imiona+=["Adam","Ewa"]  zamiast append do pustej listy razy dwa
laczna=[liczby, imiona]
print(laczna)

#lista.pop() - usuwa z listy. Jak jest pusty nawias to usuwa ostatni element listy Jak damy jakąś cyfrę to usunie wskazany w nawiasie element pamiętając, ze pierwszy element listy ma indeks 0.