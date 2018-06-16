artykuly =[]
artykuly += ['mleko', 'olej', 'masło', 'jabko']
pier_art = artykuly[0]
id_ost = len(artykuly)-1
ost_art = artykuly[id_ost]
ost_art2 = artykuly[-1]
print(pier_art, ost_art, ost_art2)

print("\n", "inna wersja", "\n")

artykuly2 =[]
artykuly2 += ['beton', 'kamienie', 'żwit', 'piasek', 'błoto']
id2_ost = len(artykuly2)
print(artykuly[::4])
print(artykuly[0: -1:])
print(artykuly[0: id2_ost: (id2_ost-1)])