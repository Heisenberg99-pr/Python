a = [] #Lista vuota
b = [0,3.14,('python', 0, 'stringa'), 9, [1,2,3] ]

print(b[2]) #indicizzazione

b[2] = 'nuovo valore' #sostituisce l'elemento nella posizione 2

print(b) #stampa tutta la lista b 

del(b[2]) #elimina il secondo elemento della lista 

print(b) 

b.append('ultimo elemento') #aggiunge un elemento a fine della lista

print(b)

c = b # aliesing, c è un alias di c, c e b sono legati dalla stessa lista

c[1] = None

print(b[1])

d = b[:] # clonazione, clona la lista b in una lista d

d[0] = None

print(b)
print(d)
