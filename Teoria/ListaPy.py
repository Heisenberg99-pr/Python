a = [] #Lista vuota
b = [0,3.14,('python', 0, 'stringa'), 9, [1,2,3] ]

print(b[2]) #indicizzazione -> O(1)

b[2] = 'nuovo valore' #sostituisce l'elemento nella posizione 2 -> O(1)

print(b) #stampa tutta la lista b -> O(n)

del(b[2]) #elimina il secondo elemento della lista -> O(n)

print(b) 

b.append('ultimo elemento') #aggiunge un elemento a fine della lista -> ammortizata O(1)

print(b)

c = b # aliesing, c è un alias di c, c e b sono legati dalla stessa lista

c[1] = None # -> O(1)

print(b[1])

d = b[:] # clonazione, clona la lista b in una lista d -> O(n)

d[0] = None

print(b)
print(d)
