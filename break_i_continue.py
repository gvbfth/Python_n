"""
break

continue
"""

wynik = 0
'''
for i in range(3):
    x = int(input("Podaj liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia!")
        break
    print("Aktualny wynik to:", wynik)
'''
i = 0
while i < 3:
    x = int(input("Podaj liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia!")
        continue
    print("Aktualny wynik to:", wynik)
    i += 1
