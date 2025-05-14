'''
a = int(input())
b = int(input())

if (a > b):
    print("Wynik:", a, "jest większe od", b,".")
elif (a < b):
    print("Wynik:", a, "jest mniejsze od", b,".")
else:
    print("Wynik:", a, "jest równe", b,".")
'''

wybor = input("* - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie: ")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if(wybor == '*'):
    print(a * b)
elif(wybor == '/'):
    if(b == 0):
        print("nie dzielimy przez 0!!!")
    else:
        print(a / b)
elif(wybor == '+'):
    print(a + b)
elif(wybor == '-'):
    print(a - b)
else:
    print("Nie wybrałeś poprawnie!")




              
