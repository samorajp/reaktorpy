wartość=input("Gab mal die Zahl!!!")
if not wartość.isdigit():
    print("CYFRA DEBILU!!!")
    exit()
else:
    wartość1=int(wartość)

if wartość1<=9 and wartość>=0:
    print("Gut Wahl!!!")
else:
    print("Ausser erwartet Wert")