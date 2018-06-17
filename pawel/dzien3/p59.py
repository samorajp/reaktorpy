import random

def losowe_zdanie(liczba_słow=5):

    wyrazy =["adam", "natalia", "jabłko", "je", "żuk"]
    wynik=""
    for i in range(liczba_słow):

        wyraz = random.choice(wyrazy)
      #  print(wyraz)
        wynik+=wyraz + " "
    wynik+="."
    return wynik

print(losowe_zdanie(6))
