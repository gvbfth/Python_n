definicje = {'imie': 'Michał'}
while(True):
    print("1: Dodaj")
    print("2: Szukaj")
    print("3: Usuń")
    print("4: Zakończ")

    wybor = int(input("Które działanie? "))

    if wybor == 1:
        klucz = input("Podaj klucz: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
    elif wybor == 2:
        klucz = input("Podaj klucz: ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie ma takiego klucza!", klucz)
    elif wybor == 3:
        klucz = input("Podaj klucz, który chcesz usunąć: ")
        if klucz in definicje:
            del definicje[klucz]
        else:
            print("Nie ma takiego klucza!", klucz)
    elif wybor == 4:
        break
      
