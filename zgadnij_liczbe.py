szukanaLiczba = 40
zgadywanaLiczba = 0


while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Odgadnij liczbe: "))

    if (zgadywanaLiczba > szukanaLiczba):
        print("za duża")
    elif (zgadywanaLiczba < szukanaLiczba):
        print("za mała")
    else:
        print("BRAWO!")
