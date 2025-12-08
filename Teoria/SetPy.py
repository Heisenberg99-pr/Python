"""
La funzione set() in python permette di creare insiemi di valori senza duplicati
e ordinati

esempio: 
"""
a = set([1,2,1,6,7,5,0,6]) # output {0, 1, 2, 5, 6, 7}
print (1 in a) # output True

a.add(10) # aggiunge un elemento alla lista
print(a)
a.remove(5) # rimuove un elemento dalla lista
print(a) 
print(len(a))