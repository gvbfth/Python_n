A = {1, 4, 20, -4, 20}
'''
B = [2, 5, 7, -1, 5]

print(set(B)) # zmaina listy w zbór
'''

B = {2, 5, 20, -1, 5}

print(A&B) #wspólne elementy
print(A|B) #łącznie wszystkie elementy
print(A-B) #zbiór elementów A, których nie ma w B
print(A^B) #wyklucza wspólne wartości
print(A)
