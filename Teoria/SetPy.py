"""
La funzione set() in python permette di creare insiemi di valori senza duplicati
e NON ordinati (l'ordine visualizzato è casuale/legato all'hash dei valori).
"""

a = set([1,2,1,6,7,5,0,6]) # Creazione da lista di n elementi -> O(n)
print (1 in a) # Appartenenza (ricerca con Hash Table) -> O(1) in media

a.add(10) # Aggiunta di un elemento -> O(1) in media
print(a) # Stampa dell'insieme (scorre n elementi) -> O(n)

a.remove(5) # Rimozione di un elemento specifico -> O(1) in media
print(a) # Stampa dell'insieme -> O(n)

print(len(a)) # Restituisce la dimensione dell'insieme -> O(1)