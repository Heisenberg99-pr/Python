'''
Scrievere una funzione che inverti una lista L

'''

def inverti_lista(L):
    '''
    Parametri: L una lista di interi

    La funzione restituisce la lista invertita
    '''
    lunghezza = len(L)
    
    if lunghezza <= 1:
        return L
    
    lx,rx = 0,lunghezza-1

    while lx <= rx:
        L[lx],L[rx] = L[rx], L[lx]
        lx += 1
        rx -= 1
    
    return L 

lista = [1,2,3,6,9,8,11]
print(f"La stringa inveritita e': {inverti_lista(lista)}")