rzymskie = {
    1: 'I',
    2: 'II',
    3: 'I' * 3,  # 'I' * 3 = 'I' + 'I' + 'I' = 'III'
    4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII',
    8: 'VIII', 9: 'IX',
    10: 'X'
}
liczba = int(input("Podaj liczbę: "))
po_rzymsku = rzymskie[liczba]
print(po_rzymsku)



