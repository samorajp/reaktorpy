lata=float(input("ile lat oszczędzamy? :\n"))
kasa=float(input("ile kasy wpłacasz? : \n"))
procent=float(input("jakie jest oprocentowanie lokaty? : \n"))

wynik=kasa*((1+(procent/100))**lata)
print(wynik)