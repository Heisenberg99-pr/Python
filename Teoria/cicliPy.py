'''
In questo file vedremmo il funzionamento dei cicli

Esistono due tipi di cicli:

for: permette di iterare su una sequenza di elementi, ad esempio: liste, stringhe, etc
while: permette di ripetere un blocco di codice fintanto che una condizione è vera

Vediamo quindi la loro struttura e il loro comportamento
'''

lista = [1,2,"Catanzaro", True,3.14]

for x in lista: # Per ogni elemento x, contenuto nella lista, esegui
    print(x) # Funzione

'''
All'inizio quindi dichiaramo il tiplo di ciclo, in questo caso for
dopodiché andiamo a dichiarare una variabile che funzionerà come 
contenitore dei singoli valori [x] e infine la variabile da etinerare [lista]

Dopo la dichirazione, subito corpo troviamo il blocco di istuzioni
che in questo caso è semplicemente un print(x)
'''

i = 0

while i < len(lista): # Mentre i è minore della lunghezza della lista, esegui
    print(lista[i]) # Funzione
    i += 1 # Incremento di i, altrimenti il ciclo sarebbe infinito

'''
Come prima dichiariamo il tipo di ciclo, in questo caso while
dopodiché dichiriamo una variabile [i] che funzionerà da indice
e infine la condizione che deve essere vera per eseguire il ciclo
dopo la dichiarazione troviamo il blocco di istruzioni
che in questo caso stampa l'elemento della lista nella posizione i
e infine incrementa i da 1, altrimenti la condizione sarebbe sempre vera
e quindi il ciclo sarebbe infinito.

Un modo per terminare un ciclo è quello di utilizzare funzione break
la quale va interromepre il ciclo, ad esempio:
'''

i = 0

while i < len(lista):
    if lista[i].type()== str:
        break # Interrompe il ciclo se l'elemento è una stringa
    print(lista[i])
    i += 1

"""
Ciclo for con enumerate:
In questo caso, andiamo a etinerare sia l'indice che il valore dell'elemento, ad esempio:
"""

a = "abcdefgh"

for i, x in enumerate(a):
    print( i, x )
#costo O(n) dove n è la linghezza della stringa a
