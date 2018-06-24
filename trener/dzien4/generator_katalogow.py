import os

f = open("studenci.txt")

for linia in f:
    identyfikator = linia.strip()
    if not os.path.isdir(identyfikator):
        os.mkdir(identyfikator)
        print("Tworzę katalog")
    else:
        print("Nie tworzę")
