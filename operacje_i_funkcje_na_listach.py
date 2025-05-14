#len() - długość (length)
#.append - dodać
#.extend - rozszerzyć
#.insert(index, co) - wstawić
#.index - indeks danego elementu
#sort(reverse=False) - sortuj rosnąco
#max()
#min()
#.count - ile razy coś wystąpi
#.pop - usuń ostatni element
#.remove - usuń pierwsze wystąpienie
#.clear - wyczyść listę
#.reverse - zamień kolejność

lista1 = [54, 1, -2, 20, 1]
lista2 = ["Arkadiusz", "Wioletta"]


#print(len(lista1))

#lista1.append(4)
#lista1.extend([2,12,24,2])
#lista1.append([2,12,24,2])
lista2.insert(0, "Kuba")
print(lista2)

print(lista1)
print(lista1.index(54))
lista1.sort(reverse=True)
print(max(lista1))
print(min(lista1))
print(lista1.count(1))
lista1.pop()
lista1.remove(1)
#lista1.clear()
lista1.reverse()

print(lista1)

