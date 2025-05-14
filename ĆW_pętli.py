wynik = 0
'''
i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik dodawania liczb:", wynik)
'''
'''
for i in range(4):
    x = int(input("Podaj liczbę: "))
    wynik += x
    

print("Wynik dodawania liczb:", wynik)
'''
'''
for i in range(1201):
    if (i % 2 == 0):
        print("Liczba", i, " jest parzysta")

print("Wynik dodawania liczb:", wynik)
'''

for i in range(200):
    if (i % 5 == 0):
        if(i % 7 != 0):
            print("Liczba", i, " jest podzielna przez 5, ale nie przez 7")

print("Wynik dodawania liczb:", wynik)
