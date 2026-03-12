'''
Definire la funzione second_max(), seguendo le specifiche:
 Parametri: L una lista di numeri
        
        Ritorna il secondo valore più grande della lista L;
        se la lista contiene almeno due elementi, None altrimenti.
        
        Nel caso di due massimi, la funzione ritorna il massimo

        Esempi:
        
        se L = [3, 1, 4, 2, 0], la funzione ritorna 3
        se L = [3, 1, 4, 2, 4], la funzione ritorna 4
'''

def second_max(L):
    '''
     Parametri: L una lista di numeri
        
        Ritorna il secondo valore più grande della lista L;
        se la lista contiene almeno due elementi, None altrimenti.
        
        Nel caso di due massimi, la funzione ritorna il massimo

        Esempi:
        
        se L = [3, 1, 4, 2, 0], la funzione ritorna 3
        se L = [3, 1, 4, 2, 4], la funzione ritorna 4
    '''
    if( len(L) < 2 ):
        return None
    max1, max2 = L[0],L[1] # Dove max1 è il primo massimo e max2 il secondo 
    
    if max2 > max1:
        max1,max2 = max2,max1

    for i in range(len(L)):
        if max1 < L[i]: 
            max2 = max1
            max1 = L[i]
        elif L[i] > max2:
            max2 = L[i]
    return max2
# Costo temporale O(n) Costo spaziale O(1)

lista = [2,3,1,8,9,0,21]
print(f"Il secondo massimo e' {second_max(lista)}")





