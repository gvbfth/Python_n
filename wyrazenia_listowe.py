liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
'''
for element in liczby:
    potegiDwojki.append(element**2)
'''
liczbyParzyste = []
'''
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)
'''

potegiDwojki2 = [element**2
                 for element in liczby
                 ]

liczbyParzyste = [element
                  for element in liczby
                  if (element % 2 == 0)
                  ]
'''
1. co zrobic na elemencie
2. podajemy skad mamy ten element
3. warunek oparty na elemncie
WYNIK: lista wygenerowana
'''
