def ricerca_binaria (l, k): 
    """
    Parametri: L, una lista ordinata secondo <=; k un valore
    Ritorna la posizione di una occorrenza di k in L, 
    k non è presente in L ritorna -1
    """
    n = len(l)

    lx,rx = 0, n

    while lx < rx-1: 
        cx = int((lx+rx)/2)

        if l[cx] == k: 
            return cx
        if k<l[cx]:
            rx=cx
        else: 
            lx = cx+1
    
    return -1

Lista = [2,3,4,7,9,10]
k = 7
print(ricerca_binaria(Lista,k))

"""
La ricerca binaria riduce di molto il costo della ricerca normale
portandolo da O(n) a O(log(n))
"""