"""
Scrivere un programma ricorsivo che stampi tutti i sottoinsiemi degli elementi
dati in input
"""

def insieme_potenza(elementi, indice = 0, sottoinsieme_corrente = []):
    #Caso base : Se la lunghezza dell'indice è uguale alla lunghezza di elementi, allora stampa sottoinsime_corrente
    if indice == len(elementi):
        print(sottoinsieme_corrente)
        return 
    #Componente ricorsiva 
    insieme_potenza(elementi, indice + 1, sottoinsieme_corrente)
    sottoinsieme_corrente.append(elementi[indice])
    insieme_potenza(elementi,indice + 1, sottoinsieme_corrente)
    sottoinsieme_corrente.pop()

elementi = ['A','B','C']

print(insieme_potenza(elementi))

    