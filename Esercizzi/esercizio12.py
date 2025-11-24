def argmax( L, i = 0):
    """
    Parametri: L una lista di valori confrontabili tra di loro, un indice della lista (i<n)
    Ritorna la posizione del massimo tra gli elementi L[i], L[i+1],...,L[n-1] se n > 0, altrimenti None
    """
    n = len(L)
    if n == 0:
        return None
    if i == n-1:
        return i

    p = argmax( L, i+1 )
    if L[i] > L[p]:
        return i
    else:
        return p
    
L = [3,5,6,4]
print(argmax(L))