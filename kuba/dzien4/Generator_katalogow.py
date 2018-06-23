import os
f = open("studenci.txt")

for linia in f:
    identyfikator = linia.strip()
    if os.path.isdir(identyfikator):
        os.rmdir(identyfikator)
        print("Tworzę katalog")
    else:
        print("Nie tworzę")