'''
Data un lista di numeri, riordinarla in ordine crescete
'''
numeri = [6, 2, 9, 1, 5, 8]

for i in range(len(numeri)):
    ordinata = True
    for j in range(i+1, len(numeri)):
        if numeri[i] > numeri[j]:
            ordinata = False
            numeri[i], numeri[j] = numeri[j], numeri[i]
    if ordinata:
        break
print(numeri)