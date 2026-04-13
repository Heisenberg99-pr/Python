'''
1) Scrivere una funzione che prenda in input una lista
e restituisca la somma degli elementi 

2) Scrivere una funzione che conti i numeri pari in una lista L

3) Scrivere una funzione che riestituisca l'elemento massimo in una
lista L
'''
#1
def somma_lista(L):
    '''
    Parametri: L una lista di interi

    La funzione somma gli elementi e restituisce il risultato della somma

    '''
    n = len(L)
    somma = 0

    for i in range(n):
        somma += L[i] 

    return somma
#2
def conta_pari(L):
    '''
    Parametri: L una lista di interi

    La funzione ritorna il numero degli elementi pari in L
    '''
    counter = 0

    for x in L:
        if x % 2 == 0:
            counter += 1 
    return counter
#3
def trova_massimo(L):
    '''
    Parametri: L una lista di interi

    La funzione ritorna l'elemento massimo nella lista
    '''
    massimo = L[1]

    for x in L :
        if(massimo < x):
            massimo = x
    return massimo

lista = [1,2,3,6,9,8]
print(f"La somma degli elementi e': {somma_lista(lista)}")
print(f"Il numero di elementi pari contenuti nella lista e': {conta_pari(lista)}")
print(f"L'elemento massimo della lista e': {trova_massimo(lista)}")