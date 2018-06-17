krotka = "01","01","2018"

print("Data ważności =" , krotka)

import datetime
dzis = datetime.datetime.now()
print("Data scu artykułu to: ",str(dzis.day) + "-"+ str(dzis.month) + "-" + str(dzis.year))
