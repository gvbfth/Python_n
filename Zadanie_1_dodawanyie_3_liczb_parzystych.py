i = 0
wynik = 0
while i < 3:
    x = int(input("Podaj liczbę:"))
    if(x % 2 ==0):
        if (x > 0):
            wynik += x
        else:
            print("Podaj liczbe dodatnią")
            continue
    else:
        print("Podaj liczbe parzystą")
        continue
    i += 1

print("To jest wynik:", wynik)
