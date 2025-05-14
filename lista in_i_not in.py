# in
# not in
# Operacje na listach

imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian", "Wojtek"]
liczby = [2, 3, 12, 24, 7, -8]

#print("Arkadiusz" in imiona)
'''
if ("Jan" in imiona):
    print("Cześć Jan!")
'''
if (2 not in liczby):
    print("Nie ma liczby 2")
else:
    print("JEST 2")
    
print(3 * liczby)

print([4, 20, 15] + liczby)
liczby = [4, 20, 15] + liczby
print(liczby)
